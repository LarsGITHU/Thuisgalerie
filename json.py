import http.client, urllib.parse, json

key = 'Ostta0g5'

try:
    conn = http.client.HTTPSConnection('www.rijksmuseum.nl')
    req = "/api/nl/collection?key=" + key + "&format=json&ps=20&p=2"
    conn.request("GET", req)

    response = conn.getresponse()
    responsetext = response.read()
    conn.close()
    resjson = json.loads(responsetext)
    print(resjson)

except Exception as e:
    print("Fout: {} {}".format(e.errno, e.strerror))