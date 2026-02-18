import urllib.request

try:
    file_name = "digital_image_processing.jpg"
    website = "http://tutorialspoint.com/java_dip/images/" + file_name

    print("Downloading File From:", website)

    with urllib.request.urlopen(website) as response:
        with open(file_name, "wb") as output_file:
            while True:
                buffer = response.read(2048)
                if not buffer:
                    break
                print("Buffer Read of length:", len(buffer))
                output_file.write(buffer)

    print("Download completed!")

except Exception as e:
    print("Exception:", str(e))
