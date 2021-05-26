// ==UserScript==
// @name         3DES Decrypt
// @namespace    http://tampermonkey.net/
// @version      2.0
// @description  Desencriptar un codigo cifrado
// @author       Marcos Fantóval C.
// @match        https://raw.githubusercontent.com/MarcosFantoval2/Criptografia/main/Tarea3/pagina.html
// @grant        none
// @require      https://cdnjs.cloudflare.com/ajax/libs/crypto-js/4.0.0/crypto-js.min.js
// ==/UserScript==
(function decryp() {
    'use strict';
   
    var iv ="12345678";
    var key = "DESllave";
    function decryptByDES(ciphertext, key, iv) {
        var keyH = CryptoJS.enc.Utf8.parse(key);
        var ivH = CryptoJS.enc.Hex.parse(CryptoJS.enc.Utf8.parse(iv).toString(CryptoJS.enc.Hex));
        var decrypted = CryptoJS.TripleDES.decrypt(ciphertext, keyH, { iv: ivH, mode: CryptoJS.mode.CBC, padding:CryptoJS.pad.Pkcs7 });
        return decrypted;
    }
    
    var div = document.getElementsByTagName("div");
    var idTextoCifrado = div[0].id;
    var mensaje_tx_plano = decryptByDES(idTextoCifrado,key, iv);
    mensaje_tx_plano = mensaje_tx_plano.toString(CryptoJS.enc.Utf8);

    div[0].innerHTML = 'mensaje cifrado: '+mensaje_tx_plano;
    console.log(mensaje_tx_plano.toString(CryptoJS.enc.Utf8))
})();