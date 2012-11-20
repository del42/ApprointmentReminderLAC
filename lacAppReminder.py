
def get(self):
        self.response.out.write("""<!DOCTYPE html "-//W3C//DTD XHTML 1.0 Strict//EN"
            "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
            <html xmlns="http://www.w3.org/1999/xhtml">
            <head>
                <meta http-equiv="content-type" content="text/html; charset=utf-8"/>
                <title>Google Maps JavaScript API Example</title>
                <script src="http://maps.google.com/maps?file=api&amp;v=2&amp;key=AIzaSyCQTH2PCkb6aargyjaJ8rvSOPmkpL_Td_E&sensor=true_or_false"
                type="text/javascript"></script>
            <script type="text/javascript">
        
            function initialize() {
                if (GBrowserIsCompatible()) {
                    var map = new GMap2(document.getElementById("map_canvas"));
                    map.setCenter(new GLatLng(37.722549,-122.441062), 13);
                    map.setUIToDefault();
                }
            }
        
            </script>
            </head>
            <body onload="initialize()" onunload="GUnload()">
            <div id="map_canvas" style="width: 800px; height: 500px"></div>
            </body>
            </html>""")

        