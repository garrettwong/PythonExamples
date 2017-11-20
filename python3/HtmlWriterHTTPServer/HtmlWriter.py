class HtmlWriter:
    def __init__(self):
        with open('css/style.css') as f:
            self.css = f.read()
            print(self.css)

        with open('js/script.js') as f:
            self.js = f.read()
            print(self.js)

    def writeHtml(self, wfile, path):
        wfile.write(bytes("<html><head><title>Python Server 3.6.</title>", "utf-8"))
        wfile.write(bytes("<style>" + self.css + "</style>", "utf-8"))
        wfile.write(bytes("</head>", "utf-8"))
        wfile.write(bytes("""
        <body>
            <nav class="container">
                <h2>Python Web Automation Server 3.6</h2>
            </nav>
            <div class="container">
                <form>
                    <input type='text' />

                    <button type="button" id="btnSubmit" class="btn btn-primary">Submit</button>

                </form>
        """, "utf-8"))
        wfile.write(bytes("<p>You accessed path: %s</p>" % path, "utf-8"))
        wfile.write(bytes("</div>", "utf-8"))
        wfile.write(bytes("<script>" + self.js + "</script>", "utf-8"))
        wfile.write(bytes("</body></html>", "utf-8"))
        
# h = HtmlWriter()