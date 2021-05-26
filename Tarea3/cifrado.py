from des import DesKey
from base64 import b64encode

data = b'tarea numero 3'
iv =b"12345678"
key = DesKey(b"DESllave")
key.is_triple()

encryption = key.encrypt(data, initial=iv, padding=True)
encryption = b64encode(encryption).decode('utf-8')
print(encryption)

html ="""<p>Este sitio contiene un mensaje secreto</p>
<div class='tripleDES' id='"""+encryption+"""'></div>
<script src="https://cdnjs.cloudflare.com/ajax/libs/crypto-js/4.0.0/crypto-js.min.js" integrity="sha512-nOQuvD9nKirvxDdvQ9OMqe2dgapbPB7vYAMrzJihw5m+aNcf0dX53m6YxM4LgA9u8e9eg9QX+/+mPu8kCNpV2A==" crossorigin="anonymous" referrerpolicy="no-referrer"></script>
<script src="./tamper.js"></script>"""

archivo = open("pagina.html","w")
archivo.write(html)
archivo.close()