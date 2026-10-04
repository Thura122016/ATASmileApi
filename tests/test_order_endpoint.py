import importlib.util
import json
from pathlib import Path
import sys
import types
import unittest
from unittest.mock import Mock, patch


ROOT = Path(__file__).resolve().parents[1]


def load_source_module(name, filename):
    spec = importlib.util.spec_from_file_location(name, ROOT / filename)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class OrderEndpointTests(unittest.TestCase):
    def setUp(self):
        # Load only the checked-in, blank template, never a merchant's ATAConfig.py.
        config = load_source_module("ATAConfig", "ATAConfig_.py")
        config.SMILE_URL = "https://merchant.example.invalid"
        config.SMILE_UID = "test-merchant"
        config.SMILE_EMAIL = "test@example.invalid"
        config.SMILE_KEY = "test-key"

        # Replace the HTTP module before loading production code. No requests
        # dependency, credentials, network calls, or live orders are needed.
        requests_stub = types.ModuleType("requests")
        self.post = Mock()
        self.response = Mock()
        self.response.json.return_value = {"test_response": "ok"}
        self.post.return_value = self.response
        requests_stub.post = self.post

        with patch.dict(sys.modules, {"ATAConfig": config, "requests": requests_stub}):
            utils = load_source_module("ATAutils", "ATAutils.py")
            with patch.dict(sys.modules, {"ATAutils": utils}):
                self.api = load_source_module("ATASmileApi", "ATASmileApi.py")

    def assert_request(self, expected_path, operation, region):
        self.post.assert_called_once()
        args, kwargs = self.post.call_args
        self.assertEqual(args, ("https://merchant.example.invalid" + expected_path,))
        self.assertEqual(kwargs["timeout"], 10)
        self.assertEqual(kwargs["json"]["product"], "test-product")
        self.assertEqual(kwargs["json"]["productid"], "test-product-id")
        self.assertEqual(kwargs["json"]["userid"], "test-player")
        self.assertEqual(kwargs["json"]["zoneid"], "test-zone")
        self.assertEqual(kwargs["json"]["uid"], "test-merchant")
        self.assertIn("sign", kwargs["json"])
        self.response.raise_for_status.assert_called_once_with()
        self.assertTrue(operation["apiOK"])
        self.assertEqual(operation["region"], region)
        self.assertEqual(operation["response"], {"test_response": "ok"})

    def create_order(self, **kwargs):
        return json.loads(self.api.createOrder(
            "test-product", "test-product-id", "test-player", "test-zone", **kwargs
        ))

    def test_default_region_order_uses_create_order_endpoint(self):
        result = self.create_order()
        self.assert_request("/br/smilecoin/api/createorder", result, "br")
        self.assertEqual(result["requestTitle"], "create-order")

    def test_global_order_has_no_region_prefix(self):
        result = self.create_order(region="global")
        self.assert_request("/smilecoin/api/createorder", result, "global")

    def test_order_preserves_explicit_region(self):
        result = self.create_order(region="test-region")
        self.assert_request("/test-region/smilecoin/api/createorder", result, "test-region")

    def test_role_check_keeps_role_endpoint(self):
        result = json.loads(self.api.checkRole(
            "test-product", "test-product-id", "test-player", "test-zone"
        ))
        self.assert_request("/br/smilecoin/api/getrole", result, "br")
        self.assertEqual(result["requestTitle"], "check-role")

    def test_global_role_check_keeps_role_endpoint(self):
        result = json.loads(self.api.checkRole(
            "test-product", "test-product-id", "test-player", "test-zone", region="global"
        ))
        self.assert_request("/smilecoin/api/getrole", result, "global")


if __name__ == "__main__":
    unittest.main()
