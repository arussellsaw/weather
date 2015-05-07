#!/usr/bin/python2.7

import requests
import shutil
import subprocess
import time

maptype = {
"wind": "wind.zip",
"waves": "waves.zip",
"press": "pressure.zip",
"rain": "rain.zip",
"clouds": "clouds.zip",
"visibility": "visibility.zip",
}

for key in maptype.keys():
    file = maptype[key]
    r = requests.get("http://passageweather.com/maps/azores/"+key+"/"+file, stream=True)
    if r.status_code == 200:
        print(key+"/"+file)
        with open (key+"/"+file, "wb+") as zipped:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, zipped)
    subprocess.Popen("/usr/bin/unzip -o "+key+"/"+file+" -d "+key+"/", shell=True)
    time.sleep(1)
    subprocess.Popen("/usr/bin/convert -delay 60 -loop 0 "+key+"/*.png "+key+".gif", shell=True)
