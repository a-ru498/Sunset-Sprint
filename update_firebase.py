import re
import os

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace script tag and add firebase init
content = content.replace('<script>\n    const canvas = document.getElementById("game");', '''<script type="module">
    import { initializeApp } from "https://www.gstatic.com/firebasejs/10.11.0/firebase-app.js";
    import { getFirestore, collection, addDoc, query, orderBy, limit, onSnapshot } from "https://www.gstatic.com/firebasejs/10.11.0/firebase-firestore.js";

    const firebaseConfig = {
      apiKey: "AIzaSyApN4vGD-aZSEws7zrhx4haxuX_Kfkr9kM",
      authDomain: "index-3183a.firebaseapp.com",
      projectId: "index-3183a",
      storageBucket: "index-3183a.firebasestorage.app",
      messagingSenderId: "636647009228",
      appId: "1:636647009228:web:c9d1c1533a6a5cd67acb69",
      measurementId: "G-5SXEHBB0D4"
    };

    const app = initializeApp(firebaseConfig);
    const db = getFirestore(app);

    const canvas = document.getElementById("game");''')

content = content.replace('<script>\r\n    const canvas = document.getElementById("game");', '''<script type="module">\r
    import { initializeApp } from "https://www.gstatic.com/firebasejs/10.11.0/firebase-app.js";\r
    import { getFirestore, collection, addDoc, query, orderBy, limit, onSnapshot } from "https://www.gstatic.com/firebasejs/10.11.0/firebase-firestore.js";\r
\r
    const firebaseConfig = {\r
      apiKey: "AIzaSyApN4vGD-aZSEws7zrhx4haxuX_Kfkr9kM",\r
      authDomain: "index-3183a.firebaseapp.com",\r
      projectId: "index-3183a",\r
      storageBucket: "index-3183a.firebasestorage.app",\r
      messagingSenderId: "636647009228",\r
      appId: "1:636647009228:web:c9d1c1533a6a5cd67acb69",\r
      measurementId: "G-5SXEHBB0D4"\r
    };\r
\r
    const app = initializeApp(firebaseConfig);\r
    const db = getFirestore(app);\r
\r
    const canvas = document.getElementById("game");''')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Done")
