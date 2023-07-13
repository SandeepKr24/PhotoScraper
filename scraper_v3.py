from bing_image_downloader import downloader

query_string = str(input("Name: "))
limit = int(input("Number of images: "))

downloader.download(query_string, limit,  output_dir='dataset', 
adult_filter_off=True, force_replace=False, timeout=60)