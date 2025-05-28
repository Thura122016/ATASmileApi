from ATAutils import create_fullData,create_fullUrl,send_json_request
import json

def checkServerList(product: str):
    try:
        payload = {'product' : product}
        fulldata = create_fullData(payload)
        fullUrl = create_fullUrl("get_server_list")
        responseData = send_json_request(fullUrl, fulldata)
        return json.dumps({"apiOK": True, "requestTitle": "check-server", "product": product, "response": responseData})
    except Exception as e:
        return json.dumps({"apiOK": False, "requestTitle": "check-server", "product": product, "response": str(e)})

def checkProduct(product: str, region: str = "br"):
    try:
        payload = {'product' : product}
        fulldata = create_fullData(payload)
        fullUrl = create_fullUrl("get_product",region)
        responseData = send_json_request(fullUrl, fulldata)
        return json.dumps({"apiOK": True, "requestTitle": "check-product", "product": product,"region": region, "response": responseData})
    except Exception as e:
        return json.dumps({"apiOK": False, "requestTitle": "check-product", "product": product,"region": region, "response": str(e)})

def checkProductList(product: str, region: str = "br"):
    try:
        payload = {'product' : product}
        fulldata = create_fullData(payload)
        fullUrl = create_fullUrl("get_product_list",region)
        responseData = send_json_request(fullUrl, fulldata)
        return json.dumps({"apiOK": True, "requestTitle": "check-product-list", "product": product,"region": region, "response": responseData})
    except Exception as e:
        return json.dumps({"apiOK": False, "requestTitle": "check-product-list", "product": product,"region": region, "response": str(e)})

def checkPoints(product: str, region: str = "br"):
    try:
        payload = {'product' : product}
        fulldata = create_fullData(payload)
        fullUrl = create_fullUrl("get_query_points",region)
        responseData = send_json_request(fullUrl, fulldata)
        return json.dumps({"apiOK": True, "requestTitle": "check-points", "product": product,"region": region, "response": responseData})
    except Exception as e:
        return json.dumps({"apiOK": False, "requestTitle": "check-points", "product": product,"region": region, "response": str(e)})
    
def checkRole(product: str,productid: str,userid: str, zoneid: str, region: str = "br"):
    try:
        payload = {
            'product' : product,
            'productid' : productid,
            'userid' : userid,
            'zoneid' : zoneid
            }
        fulldata = create_fullData(payload)
        fullUrl = create_fullUrl("get_role",region)
        responseData = send_json_request(fullUrl, fulldata)
        return json.dumps({"apiOK": True, "requestTitle": "check-role", "product": product,"region": region,'productid' : productid, 'userid' : userid, 'zoneid' : zoneid, "response": responseData})
    except Exception as e:
        return json.dumps({"apiOK": False, "requestTitle": "check-role", "product": product,"region": region, 'productid' : productid, 'userid' : userid, 'zoneid' : zoneid, "response": str(e)})

def createOrder(product: str,productid: str,userid: str, zoneid: str, region: str = "br"):
    try:
        payload = {
            'product' : product,
            'productid' : productid,
            'userid' : userid,
            'zoneid' : zoneid
            }
        fulldata = create_fullData(payload)
        fullUrl = create_fullUrl("get_role",region)
        responseData = send_json_request(fullUrl, fulldata)
        return json.dumps({"apiOK": True, "requestTitle": "create-order", "product": product,"region": region,'productid' : productid, 'userid' : userid, 'zoneid' : zoneid, "response": responseData})
    except Exception as e:
        return json.dumps({"apiOK": False, "requestTitle": "create-order", "product": product,"region": region, 'productid' : productid, 'userid' : userid, 'zoneid' : zoneid, "response": str(e)})

def checkRoleMCGG(userid: str, zoneid: str, region: str = "br"):
    try:
        payload = {
            "uid":userid,
            "sid":zoneid,
            "checkrole":"1"
            }
        fullUrl = create_fullUrl("get_role_mcgg",region)
        responseData = send_json_request(fullUrl, payload)
        return json.dumps({"apiOK": True, "requestTitle": "check-role", "product": "magicchessgogo","region": region, 'userid' : userid, 'zoneid' : zoneid, "response": responseData})
    except Exception as e:
        return json.dumps({"apiOK": False, "requestTitle": "check-role", "product": "magicchessgogo","region": region, 'userid' : userid, 'zoneid' : zoneid, "response": str(e)})