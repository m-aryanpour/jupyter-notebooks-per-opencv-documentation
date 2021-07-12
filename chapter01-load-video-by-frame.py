Python 3.8.10 | packaged by conda-forge | (default, May 11 2021, 06:25:23) [MSC v.1916 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
 RESTART: F:/Users/Administrator/Downloads/examine-image-filters-09Jul2021.py 
>>> # Run Region [17-18]
Downloading data from https://storage.googleapis.com/download.tensorflow.org/data/imagenet_class_index.json
Traceback (most recent call last):
  File "F:\Anaconda3\envs\deepxde\lib\site-packages\tensorflow\python\keras\utils\data_utils.py", line 278, in get_file
    urlretrieve(origin, fpath, dl_progress)
  File "F:\Anaconda3\envs\deepxde\lib\urllib\request.py", line 247, in urlretrieve
    with contextlib.closing(urlopen(url, data)) as fp:
  File "F:\Anaconda3\envs\deepxde\lib\urllib\request.py", line 222, in urlopen
    return opener.open(url, data, timeout)
  File "F:\Anaconda3\envs\deepxde\lib\urllib\request.py", line 531, in open
    response = meth(req, response)
  File "F:\Anaconda3\envs\deepxde\lib\urllib\request.py", line 640, in http_response
    response = self.parent.error(
  File "F:\Anaconda3\envs\deepxde\lib\urllib\request.py", line 569, in error
    return self._call_chain(*args)
  File "F:\Anaconda3\envs\deepxde\lib\urllib\request.py", line 502, in _call_chain
    result = func(*args)
  File "F:\Anaconda3\envs\deepxde\lib\urllib\request.py", line 649, in http_error_default
    raise HTTPError(req.full_url, code, msg, hdrs, fp)
urllib.error.HTTPError: HTTP Error 403: Forbidden

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 18, in <module>
  File "F:\Anaconda3\envs\deepxde\lib\site-packages\tensorflow\python\keras\applications\vgg16.py", line 236, in decode_predictions
    return imagenet_utils.decode_predictions(preds, top=top)
  File "F:\Anaconda3\envs\deepxde\lib\site-packages\tensorflow\python\keras\applications\imagenet_utils.py", line 153, in decode_predictions
    fpath = data_utils.get_file(
  File "F:\Anaconda3\envs\deepxde\lib\site-packages\tensorflow\python\keras\utils\data_utils.py", line 280, in get_file
    raise Exception(error_msg.format(origin, e.code, e.msg))
Exception: URL fetch failure on https://storage.googleapis.com/download.tensorflow.org/data/imagenet_class_index.json: 403 -- Forbidden
>>> # Run Region [line 18]
Downloading data from https://storage.googleapis.com/download.tensorflow.org/data/imagenet_class_index.json
Traceback (most recent call last):
  File "F:\Anaconda3\envs\deepxde\lib\site-packages\tensorflow\python\keras\utils\data_utils.py", line 278, in get_file
    urlretrieve(origin, fpath, dl_progress)
  File "F:\Anaconda3\envs\deepxde\lib\urllib\request.py", line 247, in urlretrieve
    with contextlib.closing(urlopen(url, data)) as fp:
  File "F:\Anaconda3\envs\deepxde\lib\urllib\request.py", line 222, in urlopen
    return opener.open(url, data, timeout)
  File "F:\Anaconda3\envs\deepxde\lib\urllib\request.py", line 531, in open
    response = meth(req, response)
  File "F:\Anaconda3\envs\deepxde\lib\urllib\request.py", line 640, in http_response
    response = self.parent.error(
  File "F:\Anaconda3\envs\deepxde\lib\urllib\request.py", line 569, in error
    return self._call_chain(*args)
  File "F:\Anaconda3\envs\deepxde\lib\urllib\request.py", line 502, in _call_chain
    result = func(*args)
  File "F:\Anaconda3\envs\deepxde\lib\urllib\request.py", line 649, in http_error_default
    raise HTTPError(req.full_url, code, msg, hdrs, fp)
urllib.error.HTTPError: HTTP Error 403: Forbidden

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 18, in <module>
  File "F:\Anaconda3\envs\deepxde\lib\site-packages\tensorflow\python\keras\applications\vgg16.py", line 236, in decode_predictions
    return imagenet_utils.decode_predictions(preds, top=top)
  File "F:\Anaconda3\envs\deepxde\lib\site-packages\tensorflow\python\keras\applications\imagenet_utils.py", line 153, in decode_predictions
    fpath = data_utils.get_file(
  File "F:\Anaconda3\envs\deepxde\lib\site-packages\tensorflow\python\keras\utils\data_utils.py", line 280, in get_file
    raise Exception(error_msg.format(origin, e.code, e.msg))
Exception: URL fetch failure on https://storage.googleapis.com/download.tensorflow.org/data/imagenet_class_index.json: 403 -- Forbidden
>>> help(decode_predictions)
Help on function decode_predictions in module tensorflow.python.keras.applications.vgg16:

decode_predictions(preds, top=5)
    Decodes the prediction of an ImageNet model.
    
    Arguments:
      preds: Numpy array encoding a batch of predictions.
      top: Integer, how many top-guesses to return. Defaults to 5.
    
    Returns:
      A list of lists of top class prediction tuples
      `(class_name, class_description, score)`.
      One list of tuples per sample in batch input.
    
    Raises:
      ValueError: In case of invalid shape of the `pred` array
        (must be 2D).

>>> # Run Region [line 17]
>>> decode_predictions(preds, top=3)[0]
Downloading data from https://storage.googleapis.com/download.tensorflow.org/data/imagenet_class_index.json
Traceback (most recent call last):
  File "F:\Anaconda3\envs\deepxde\lib\site-packages\tensorflow\python\keras\utils\data_utils.py", line 278, in get_file
    urlretrieve(origin, fpath, dl_progress)
  File "F:\Anaconda3\envs\deepxde\lib\urllib\request.py", line 247, in urlretrieve
    with contextlib.closing(urlopen(url, data)) as fp:
  File "F:\Anaconda3\envs\deepxde\lib\urllib\request.py", line 222, in urlopen
    return opener.open(url, data, timeout)
  File "F:\Anaconda3\envs\deepxde\lib\urllib\request.py", line 531, in open
    response = meth(req, response)
  File "F:\Anaconda3\envs\deepxde\lib\urllib\request.py", line 640, in http_response
    response = self.parent.error(
  File "F:\Anaconda3\envs\deepxde\lib\urllib\request.py", line 569, in error
    return self._call_chain(*args)
  File "F:\Anaconda3\envs\deepxde\lib\urllib\request.py", line 502, in _call_chain
    result = func(*args)
  File "F:\Anaconda3\envs\deepxde\lib\urllib\request.py", line 649, in http_error_default
    raise HTTPError(req.full_url, code, msg, hdrs, fp)
urllib.error.HTTPError: HTTP Error 403: Forbidden

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    decode_predictions(preds, top=3)[0]
  File "F:\Anaconda3\envs\deepxde\lib\site-packages\tensorflow\python\keras\applications\vgg16.py", line 236, in decode_predictions
    return imagenet_utils.decode_predictions(preds, top=top)
  File "F:\Anaconda3\envs\deepxde\lib\site-packages\tensorflow\python\keras\applications\imagenet_utils.py", line 153, in decode_predictions
    fpath = data_utils.get_file(
  File "F:\Anaconda3\envs\deepxde\lib\site-packages\tensorflow\python\keras\utils\data_utils.py", line 280, in get_file
    raise Exception(error_msg.format(origin, e.code, e.msg))
Exception: URL fetch failure on https://storage.googleapis.com/download.tensorflow.org/data/imagenet_class_index.json: 403 -- Forbidden
>>> import json
>>> import os
>>> os.getcwd()
'F:\\Users\\Administrator\\Downloads'
>>> with open('imagenet_class_index.json') as f:
	CLASS_INDEX= json.load(f)

	
>>> # Run Region [line 18]
Downloading data from https://storage.googleapis.com/download.tensorflow.org/data/imagenet_class_index.json
Traceback (most recent call last):
  File "F:\Anaconda3\envs\deepxde\lib\site-packages\tensorflow\python\keras\utils\data_utils.py", line 278, in get_file
    urlretrieve(origin, fpath, dl_progress)
  File "F:\Anaconda3\envs\deepxde\lib\urllib\request.py", line 247, in urlretrieve
    with contextlib.closing(urlopen(url, data)) as fp:
  File "F:\Anaconda3\envs\deepxde\lib\urllib\request.py", line 222, in urlopen
    return opener.open(url, data, timeout)
  File "F:\Anaconda3\envs\deepxde\lib\urllib\request.py", line 531, in open
    response = meth(req, response)
  File "F:\Anaconda3\envs\deepxde\lib\urllib\request.py", line 640, in http_response
    response = self.parent.error(
  File "F:\Anaconda3\envs\deepxde\lib\urllib\request.py", line 569, in error
    return self._call_chain(*args)
  File "F:\Anaconda3\envs\deepxde\lib\urllib\request.py", line 502, in _call_chain
    result = func(*args)
  File "F:\Anaconda3\envs\deepxde\lib\urllib\request.py", line 649, in http_error_default
    raise HTTPError(req.full_url, code, msg, hdrs, fp)
urllib.error.HTTPError: HTTP Error 403: Forbidden

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 18, in <module>
  File "F:\Anaconda3\envs\deepxde\lib\site-packages\tensorflow\python\keras\applications\vgg16.py", line 236, in decode_predictions
    return imagenet_utils.decode_predictions(preds, top=top)
  File "F:\Anaconda3\envs\deepxde\lib\site-packages\tensorflow\python\keras\applications\imagenet_utils.py", line 153, in decode_predictions
    fpath = data_utils.get_file(
  File "F:\Anaconda3\envs\deepxde\lib\site-packages\tensorflow\python\keras\utils\data_utils.py", line 280, in get_file
    raise Exception(error_msg.format(origin, e.code, e.msg))
Exception: URL fetch failure on https://storage.googleapis.com/download.tensorflow.org/data/imagenet_class_index.json: 403 -- Forbidden
>>> global CLASS_INDEX
>>> # Run Region [line 18]
Downloading data from https://storage.googleapis.com/download.tensorflow.org/data/imagenet_class_index.json
Traceback (most recent call last):
  File "F:\Anaconda3\envs\deepxde\lib\site-packages\tensorflow\python\keras\utils\data_utils.py", line 278, in get_file
    urlretrieve(origin, fpath, dl_progress)
  File "F:\Anaconda3\envs\deepxde\lib\urllib\request.py", line 247, in urlretrieve
    with contextlib.closing(urlopen(url, data)) as fp:
  File "F:\Anaconda3\envs\deepxde\lib\urllib\request.py", line 222, in urlopen
    return opener.open(url, data, timeout)
  File "F:\Anaconda3\envs\deepxde\lib\urllib\request.py", line 531, in open
    response = meth(req, response)
  File "F:\Anaconda3\envs\deepxde\lib\urllib\request.py", line 640, in http_response
    response = self.parent.error(
  File "F:\Anaconda3\envs\deepxde\lib\urllib\request.py", line 569, in error
    return self._call_chain(*args)
  File "F:\Anaconda3\envs\deepxde\lib\urllib\request.py", line 502, in _call_chain
    result = func(*args)
  File "F:\Anaconda3\envs\deepxde\lib\urllib\request.py", line 649, in http_error_default
    raise HTTPError(req.full_url, code, msg, hdrs, fp)
urllib.error.HTTPError: HTTP Error 403: Forbidden

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 18, in <module>
  File "F:\Anaconda3\envs\deepxde\lib\site-packages\tensorflow\python\keras\applications\vgg16.py", line 236, in decode_predictions
    return imagenet_utils.decode_predictions(preds, top=top)
  File "F:\Anaconda3\envs\deepxde\lib\site-packages\tensorflow\python\keras\applications\imagenet_utils.py", line 153, in decode_predictions
    fpath = data_utils.get_file(
  File "F:\Anaconda3\envs\deepxde\lib\site-packages\tensorflow\python\keras\utils\data_utils.py", line 280, in get_file
    raise Exception(error_msg.format(origin, e.code, e.msg))
Exception: URL fetch failure on https://storage.googleapis.com/download.tensorflow.org/data/imagenet_class_index.json: 403 -- Forbidden
>>> with open('imagenet_class_index.json') as f:
	CLASS_INDEX= json.load(f)

	
>>> # Run Region [line 18]
Downloading data from https://storage.googleapis.com/download.tensorflow.org/data/imagenet_class_index.json
Traceback (most recent call last):
  File "F:\Anaconda3\envs\deepxde\lib\site-packages\tensorflow\python\keras\utils\data_utils.py", line 278, in get_file
    urlretrieve(origin, fpath, dl_progress)
  File "F:\Anaconda3\envs\deepxde\lib\urllib\request.py", line 247, in urlretrieve
    with contextlib.closing(urlopen(url, data)) as fp:
  File "F:\Anaconda3\envs\deepxde\lib\urllib\request.py", line 222, in urlopen
    return opener.open(url, data, timeout)
  File "F:\Anaconda3\envs\deepxde\lib\urllib\request.py", line 531, in open
    response = meth(req, response)
  File "F:\Anaconda3\envs\deepxde\lib\urllib\request.py", line 640, in http_response
    response = self.parent.error(
  File "F:\Anaconda3\envs\deepxde\lib\urllib\request.py", line 569, in error
    return self._call_chain(*args)
  File "F:\Anaconda3\envs\deepxde\lib\urllib\request.py", line 502, in _call_chain
    result = func(*args)
  File "F:\Anaconda3\envs\deepxde\lib\urllib\request.py", line 649, in http_error_default
    raise HTTPError(req.full_url, code, msg, hdrs, fp)
urllib.error.HTTPError: HTTP Error 403: Forbidden

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 18, in <module>
  File "F:\Anaconda3\envs\deepxde\lib\site-packages\tensorflow\python\keras\applications\vgg16.py", line 236, in decode_predictions
    return imagenet_utils.decode_predictions(preds, top=top)
  File "F:\Anaconda3\envs\deepxde\lib\site-packages\tensorflow\python\keras\applications\imagenet_utils.py", line 153, in decode_predictions
    fpath = data_utils.get_file(
  File "F:\Anaconda3\envs\deepxde\lib\site-packages\tensorflow\python\keras\utils\data_utils.py", line 280, in get_file
    raise Exception(error_msg.format(origin, e.code, e.msg))
Exception: URL fetch failure on https://storage.googleapis.com/download.tensorflow.org/data/imagenet_class_index.json: 403 -- Forbidden
>>> # Run Region [20-25]
Traceback (most recent call last):
  File "<string>", line 22, in <module>
NameError: name 'top' is not defined
>>> # Run Region [20-26]
>>> results
[[('n02504458', 'African_elephant', 0.7827559), ('n02504013', 'Indian_elephant', 0.14814053), ('n01871265', 'tusker', 0.069103494), ('n02480855', 'gorilla', 4.0038945e-08), ('n02410509', 'bison', 2.6331708e-08)]]
>>> # Run Region [20-32]
predicted:  [('n02504458', 'African_elephant', 0.7827559), ('n02504013', 'Indian_elephant', 0.14814053), ('n01871265', 'tusker', 0.069103494), ('n02480855', 'gorilla', 4.0038945e-08), ('n02410509', 'bison', 2.6331708e-08)]
>>> results[0]
[('n02504458', 'African_elephant', 0.7827559), ('n02504013', 'Indian_elephant', 0.14814053), ('n01871265', 'tusker', 0.069103494), ('n02480855', 'gorilla', 4.0038945e-08), ('n02410509', 'bison', 2.6331708e-08)]
>>> with open('imagenet_class_index.json') as f:
	CLASS_INDEX= json.load(f)

	
>>> results[0]
[('n02504458', 'African_elephant', 0.7827559), ('n02504013', 'Indian_elephant', 0.14814053), ('n01871265', 'tusker', 0.069103494), ('n02480855', 'gorilla', 4.0038945e-08), ('n02410509', 'bison', 2.6331708e-08)]
>>> results[0][0]
('n02504458', 'African_elephant', 0.7827559)
>>> results[0][0:3]
[('n02504458', 'African_elephant', 0.7827559), ('n02504013', 'Indian_elephant', 0.14814053), ('n01871265', 'tusker', 0.069103494)]
>>> results[0][q:3]
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    results[0][q:3]
NameError: name 'q' is not defined
>>> results[0][1:3]
[('n02504013', 'Indian_elephant', 0.14814053), ('n01871265', 'tusker', 0.069103494)]
>>> results[1][0:3]
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    results[1][0:3]
IndexError: list index out of range
>>> 
 RESTART: F:/Users/Administrator/Downloads/examine-image-filters-09Jul2021.py 
predicted:  [('n02504458', 'African_elephant', 0.7827559), ('n02504013', 'Indian_elephant', 0.14814053), ('n01871265', 'tusker', 0.069103494), ('n02480855', 'gorilla', 4.0038945e-08), ('n02410509', 'bison', 2.6331708e-08)]
>>> 
 RESTART: F:/Users/Administrator/Downloads/examine-image-filters-09Jul2021.py 
predicted:  [('n03814906', 'necklace', 0.566971), ('n02999410', 'chain', 0.09596879), ('n03595614', 'jersey', 0.06128305), ('n03938244', 'pillow', 0.035335865), ('n03929660', 'pick', 0.022749195)]
>>> 
 RESTART: F:/Users/Administrator/Downloads/examine-image-filters-09Jul2021.py 
predicted:  [('n03903868', 'pedestal', 0.5936732), ('n03388043', 'fountain', 0.29062608), ('n03877845', 'palace', 0.057873596), ('n04486054', 'triumphal_arch', 0.03333896), ('n02699494', 'altar', 0.005821133)]
>>> 
 RESTART: F:/Users/Administrator/Downloads/examine-image-filters-09Jul2021.py 
predicted:  [('n04275548', 'spider_web', 0.099600516), ('n03888257', 'parachute', 0.052571323), ('n01770081', 'harvestman', 0.034417097), ('n03291819', 'envelope', 0.03372797), ('n02219486', 'ant', 0.027423546)]
>>> 
 RESTART: F:/Users/Administrator/Downloads/examine-image-filters-09Jul2021.py 
predicted:  [('n01930112', 'nematode', 0.5999849), ('n03532672', 'hook', 0.04858455), ('n03633091', 'ladle', 0.011469951), ('n03291819', 'envelope', 0.00883336), ('n03347037', 'fire_screen', 0.008204775)]
>>> 
 RESTART: F:/Users/Administrator/Downloads/examine-image-filters-09Jul2021.py 
predicted:  [('n04005630', 'prison', 0.33113426), ('n03355925', 'flagpole', 0.06888013), ('n02788148', 'bannister', 0.05415905), ('n03495258', 'harp', 0.038867112), ('n03854065', 'organ', 0.03846527)]
>>> 
 RESTART: F:/Users/Administrator/Downloads/examine-image-filters-09Jul2021.py 
predicted:  [('n03355925', 'flagpole', 0.08466891), ('n02879718', 'bow', 0.026849715), ('n03903868', 'pedestal', 0.022815706), ('n01818515', 'macaw', 0.020914856), ('n03787032', 'mortarboard', 0.019886836)]
>>> 
 RESTART: F:/Users/Administrator/Downloads/examine-image-filters-09Jul2021.py 
predicted:  [('n02504013', 'Indian_elephant', 0.8315843), ('n01871265', 'tusker', 0.13368383), ('n02504458', 'African_elephant', 0.027962284), ('n02398521', 'hippopotamus', 0.0030785936), ('n02134084', 'ice_bear', 0.0003861902)]
>>> 
 RESTART: F:/Users/Administrator/Downloads/examine-image-filters-09Jul2021.py 
predicted:  [('n07248320', 'book_jacket', 0.4586918), ('n06596364', 'comic_book', 0.13042474), ('n03743016', 'megalith', 0.015963607), ('n04458633', 'totem_pole', 0.015514635), ('n03930313', 'picket_fence', 0.015179945)]
>>> 
 RESTART: F:/Users/Administrator/Downloads/examine-image-filters-09Jul2021.py 
predicted:  [('n03980874', 'poncho', 0.8014515), ('n04429376', 'throne', 0.039184783), ('n04525038', 'velvet', 0.019137193), ('n04325704', 'stole', 0.014792279), ('n03347037', 'fire_screen', 0.014085322)]
>>> 
 RESTART: F:/Users/Administrator/Downloads/examine-image-filters-09Jul2021.py 
predicted:  [('n07615774', 'ice_lolly', 0.52808005), ('n04116512', 'rubber_eraser', 0.115618885), ('n04270147', 'spatula', 0.07837309), ('n02948072', 'candle', 0.06242497), ('n04476259', 'tray', 0.04533975)]
>>> # Run Region [22-43]
>>> det_img('melons-002')
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    det_img('melons-002')
  File "<string>", line 23, in det_img
  File "F:\Anaconda3\envs\deepxde\lib\site-packages\tensorflow\python\keras\preprocessing\image.py", line 300, in load_img
    return image.load_img(path, grayscale=grayscale, color_mode=color_mode,
  File "F:\Anaconda3\envs\deepxde\lib\site-packages\keras_preprocessing\image\utils.py", line 113, in load_img
    with open(path, 'rb') as f:
FileNotFoundError: [Errno 2] No such file or directory: 'melons-002'
>>> det_img('melons-001')
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    det_img('melons-001')
  File "<string>", line 23, in det_img
  File "F:\Anaconda3\envs\deepxde\lib\site-packages\tensorflow\python\keras\preprocessing\image.py", line 300, in load_img
    return image.load_img(path, grayscale=grayscale, color_mode=color_mode,
  File "F:\Anaconda3\envs\deepxde\lib\site-packages\keras_preprocessing\image\utils.py", line 113, in load_img
    with open(path, 'rb') as f:
FileNotFoundError: [Errno 2] No such file or directory: 'melons-001'
>>> os.getcwd()
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    os.getcwd()
NameError: name 'os' is not defined
>>> import os
>>> os.getcwd()
'F:\\Users\\Administrator\\Downloads'
>>> det_img('melons-001')
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    det_img('melons-001')
  File "<string>", line 23, in det_img
  File "F:\Anaconda3\envs\deepxde\lib\site-packages\tensorflow\python\keras\preprocessing\image.py", line 300, in load_img
    return image.load_img(path, grayscale=grayscale, color_mode=color_mode,
  File "F:\Anaconda3\envs\deepxde\lib\site-packages\keras_preprocessing\image\utils.py", line 113, in load_img
    with open(path, 'rb') as f:
FileNotFoundError: [Errno 2] No such file or directory: 'melons-001'
>>> det_img('melons-001.jpg')
predicted:  [('n07615774', 'ice_lolly', 0.52808005), ('n04116512', 'rubber_eraser', 0.115618885), ('n04270147', 'spatula', 0.07837309), ('n02948072', 'candle', 0.06242497), ('n04476259', 'tray', 0.04533975)]
>>> det_img('melons-002.jpg')
predicted:  [('n02892767', 'brassiere', 0.5056364), ('n02837789', 'bikini', 0.38195986), ('n03710637', 'maillot', 0.10675344), ('n03710721', 'maillot', 0.003950124), ('n04584207', 'wig', 0.00029437797)]
>>> det_img('melons-002.jpg')
predicted:  [('n02892767', 'brassiere', 0.30537152), ('n03720891', 'maraca', 0.22687529), ('n03255030', 'dumbbell', 0.1558628), ('n02808440', 'bathtub', 0.055415872), ('n04493381', 'tub', 0.04120291)]
>>> det_img('melons-002.jpg')
predicted:  [('n02834397', 'bib', 0.7935146), ('n03908714', 'pencil_sharpener', 0.03332656), ('n04116512', 'rubber_eraser', 0.01883078), ('n03720891', 'maraca', 0.017592974), ('n03840681', 'ocarina', 0.013170875)]
>>> det_img('melons-003.jpg')
predicted:  [('n03720891', 'maraca', 0.18930842), ('n03961711', 'plate_rack', 0.12918049), ('n01968897', 'chambered_nautilus', 0.076852046), ('n03445777', 'golf_ball', 0.04381385), ('n03314780', 'face_powder', 0.043683928)]
>>> det_img('melons-004.jpg')
predicted:  [('n03733281', 'maze', 0.33486998), ('n03291819', 'envelope', 0.3280778), ('n04019541', 'puck', 0.04759766), ('n03065424', 'coil', 0.031541575), ('n04259630', 'sombrero', 0.029947994)]
>>> det_img('melons-005.jpg')
predicted:  [('n04118776', 'rule', 0.17067155), ('n03291819', 'envelope', 0.13146545), ('n03476684', 'hair_slide', 0.051208984), ('n04259630', 'sombrero', 0.04698871), ('n01930112', 'nematode', 0.039402287)]
>>> det_img('cable-01')
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    det_img('cable-01')
  File "<string>", line 23, in det_img
  File "F:\Anaconda3\envs\deepxde\lib\site-packages\tensorflow\python\keras\preprocessing\image.py", line 300, in load_img
    return image.load_img(path, grayscale=grayscale, color_mode=color_mode,
  File "F:\Anaconda3\envs\deepxde\lib\site-packages\keras_preprocessing\image\utils.py", line 113, in load_img
    with open(path, 'rb') as f:
FileNotFoundError: [Errno 2] No such file or directory: 'cable-01'
>>> det_img('cable-01.jpg')
predicted:  [('n02879718', 'bow', 0.11903958), ('n04154565', 'screwdriver', 0.11569974), ('n04008634', 'projectile', 0.06355359), ('n03995372', 'power_drill', 0.03582644), ('n03720891', 'maraca', 0.035748266)]
>>> det_img('cable-02.jpg')
predicted:  [('n04141327', 'scabbard', 0.2749105), ('n04116512', 'rubber_eraser', 0.11136515), ('n03388183', 'fountain_pen', 0.11031129), ('n03658185', 'letter_opener', 0.09866942), ('n04579432', 'whistle', 0.047643483)]
>>> det_img('cable-03.jpg')
predicted:  [('n03075370', 'combination_lock', 0.39628553), ('n03065424', 'coil', 0.101469934), ('n04599235', 'wool', 0.09869239), ('n04367480', 'swab', 0.038719494), ('n02910353', 'buckle', 0.02758047)]
>>> det_img('cable-04.jpg')
predicted:  [('n04154565', 'screwdriver', 0.18923566), ('n03666591', 'lighter', 0.10653097), ('n04579432', 'whistle', 0.068154335), ('n02966687', "carpenter's_kit", 0.0654437), ('n03995372', 'power_drill', 0.057997547)]
>>> det_img('cable-05.jpg')
predicted:  [('n04286575', 'spotlight', 0.22000402), ('n04372370', 'switch', 0.095367275), ('n04557648', 'water_bottle', 0.06282354), ('n03868863', 'oxygen_mask', 0.050956976), ('n04067472', 'reel', 0.043637656)]
>>> det_img('cable-06.jpg')
predicted:  [('n03291819', 'envelope', 0.21506774), ('n03595614', 'jersey', 0.03617987), ('n03961711', 'plate_rack', 0.026270946), ('n04476259', 'tray', 0.023698097), ('n06359193', 'web_site', 0.019901566)]
>>> det_img('cable-07.jpg')
predicted:  [('n03920288', 'Petri_dish', 0.16242567), ('n03692522', 'loupe', 0.15242335), ('n03075370', 'combination_lock', 0.08436229), ('n03961711', 'plate_rack', 0.06995868), ('n01930112', 'nematode', 0.060100827)]
>>> det_img('cable-08.jpg')
predicted:  [('n04579432', 'whistle', 0.32348683), ('n03627232', 'knot', 0.31677052), ('n03532672', 'hook', 0.06322241), ('n03483316', 'hand_blower', 0.025107108), ('n03868863', 'oxygen_mask', 0.021672908)]
>>> det_img('cable-09.jpg')
predicted:  [('n03291819', 'envelope', 0.093674436), ('n03666591', 'lighter', 0.08739811), ('n04579432', 'whistle', 0.050167337), ('n03476684', 'hair_slide', 0.04907354), ('n03759954', 'microphone', 0.041471995)]
>>> 
 RESTART: F:/Users/Administrator/Downloads/examine-image-filters-09Jul2021.py 
det_img
>>> det_img(img_path[2])
predicted:  [('n03903868', 'pedestal', 0.5936732), ('n03388043', 'fountain', 0.29062608), ('n03877845', 'palace', 0.057873596), ('n04486054', 'triumphal_arch', 0.03333896), ('n02699494', 'altar', 0.005821133)]
>>> det_img('C:\Users\PC\Downloads\pics\shapes001.png')
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
>>> det_img('shapes001.png')
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    det_img('shapes001.png')
  File "F:/Users/Administrator/Downloads/examine-image-filters-09Jul2021.py", line 25, in det_img
    img = image.load_img(img_path, target_size=(224,224)) # load a reshape
  File "F:\Anaconda3\envs\deepxde\lib\site-packages\tensorflow\python\keras\preprocessing\image.py", line 300, in load_img
    return image.load_img(path, grayscale=grayscale, color_mode=color_mode,
  File "F:\Anaconda3\envs\deepxde\lib\site-packages\keras_preprocessing\image\utils.py", line 113, in load_img
    with open(path, 'rb') as f:
FileNotFoundError: [Errno 2] No such file or directory: 'shapes001.png'
>>> os.getcwd()
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    os.getcwd()
NameError: name 'os' is not defined
>>> import os
>>> os.getcwd()
'F:\\Users\\Administrator\\Downloads'
>>> det_img('shapes001.png')
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    det_img('shapes001.png')
  File "F:/Users/Administrator/Downloads/examine-image-filters-09Jul2021.py", line 25, in det_img
    img = image.load_img(img_path, target_size=(224,224)) # load a reshape
  File "F:\Anaconda3\envs\deepxde\lib\site-packages\tensorflow\python\keras\preprocessing\image.py", line 300, in load_img
    return image.load_img(path, grayscale=grayscale, color_mode=color_mode,
  File "F:\Anaconda3\envs\deepxde\lib\site-packages\keras_preprocessing\image\utils.py", line 113, in load_img
    with open(path, 'rb') as f:
FileNotFoundError: [Errno 2] No such file or directory: 'shapes001.png'
>>> det_img('shapes-001.png')
predicted:  [('n06359193', 'web_site', 0.8012212), ('n04118776', 'rule', 0.07163736), ('n03291819', 'envelope', 0.038523696), ('n02840245', 'binder', 0.012585508), ('n03782006', 'monitor', 0.008285924)]
>>> 
============== RESTART: F:/Users/Administrator/Downloads/cr1.py ==============
>>> A



>>> 
============== RESTART: F:/Users/Administrator/Downloads/cr1.py ==============
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr1.py", line 7, in <module>
    os.chdir("F:\\Users\\Administrator\Application Data\Downloads")
FileNotFoundError: [WinError 3] The system cannot find the path specified: 'F:\\Users\\Administrator\\Application Data\\Downloads'
>>> 
============== RESTART: F:/Users/Administrator/Downloads/cr1.py ==============
>>> A[0,1:10,10:10,:]
array([], shape=(9, 0, 3), dtype=float32)
>>> A.shape
(1, 400, 600, 3)
>>> A[0,1:10,11:10,:][0]
array([], shape=(0, 3), dtype=float32)
>>> A[0,1:10,:10,:][0]
array([[ 79.061   , 134.22101 , 129.32    ],
       [ 76.061   , 130.22101 , 125.32    ],
       [ 62.060997, 111.221   , 106.32    ],
       [ 44.060997,  87.221   ,  81.32    ],
       [  8.060997,  37.221   ,  31.32    ],
       [139.061   , 122.221   , 119.32    ],
       [ 91.061   ,  58.221   ,  71.32    ],
       [-17.939003, -43.779   , -37.68    ],
       [147.061   , 128.22101 , 116.32    ],
       [147.061   , 128.22101 , 116.32    ]], dtype=float32)
>>> # Run Region [9-10]
>>> A[1:10,:10,:]
array([[[253., 251., 183.],
        [253., 251., 183.],
        [253., 251., 183.],
        [251., 249., 182.],
        [249., 247., 180.],
        [245., 243., 177.],
        [241., 239., 174.],
        [236., 235., 171.],
        [230., 228., 166.],
        [223., 221., 161.]],

       [[253., 251., 183.],
        [253., 251., 183.],
        [253., 251., 183.],
        [251., 249., 182.],
        [249., 247., 180.],
        [245., 243., 177.],
        [241., 239., 174.],
        [236., 235., 171.],
        [230., 228., 166.],
        [223., 221., 161.]],

       [[253., 251., 183.],
        [253., 251., 183.],
        [253., 251., 183.],
        [251., 249., 182.],
        [249., 247., 180.],
        [245., 243., 177.],
        [241., 239., 174.],
        [236., 235., 171.],
        [230., 228., 166.],
        [223., 221., 161.]],

       [[253., 251., 183.],
        [253., 251., 183.],
        [253., 251., 183.],
        [251., 249., 182.],
        [249., 247., 180.],
        [245., 243., 177.],
        [241., 239., 174.],
        [236., 235., 171.],
        [230., 228., 166.],
        [223., 221., 161.]],

       [[253., 251., 182.],
        [253., 251., 182.],
        [253., 251., 182.],
        [251., 249., 181.],
        [249., 247., 179.],
        [245., 243., 176.],
        [241., 239., 174.],
        [236., 235., 170.],
        [230., 228., 165.],
        [223., 221., 160.]],

       [[253., 251., 182.],
        [253., 251., 182.],
        [253., 251., 182.],
        [251., 249., 181.],
        [249., 247., 179.],
        [245., 243., 176.],
        [241., 239., 174.],
        [236., 235., 170.],
        [230., 228., 165.],
        [223., 221., 160.]],

       [[253., 251., 182.],
        [253., 251., 182.],
        [253., 251., 182.],
        [251., 249., 181.],
        [249., 247., 179.],
        [245., 243., 176.],
        [241., 239., 174.],
        [236., 235., 170.],
        [230., 228., 165.],
        [223., 221., 160.]],

       [[252., 251., 182.],
        [252., 251., 182.],
        [252., 251., 182.],
        [250., 249., 181.],
        [248., 247., 179.],
        [244., 243., 176.],
        [240., 239., 174.],
        [235., 235., 170.],
        [229., 228., 165.],
        [222., 221., 160.]],

       [[252., 251., 182.],
        [252., 251., 182.],
        [252., 251., 182.],
        [250., 249., 181.],
        [248., 247., 179.],
        [244., 243., 176.],
        [240., 239., 174.],
        [235., 235., 170.],
        [229., 228., 165.],
        [222., 221., 160.]]], dtype=float32)
>>> # Run Region [line 12]
>>> A[1:10,:10,:]
array([[[ 79.061   , 134.22101 , 129.32    ],
        [ 79.061   , 134.22101 , 129.32    ],
        [ 79.061   , 134.22101 , 129.32    ],
        [ 78.061   , 132.22101 , 127.32    ],
        [ 76.061   , 130.22101 , 125.32    ],
        [ 73.061   , 126.221   , 121.32    ],
        [ 70.061   , 122.221   , 117.32    ],
        [ 67.061   , 118.221   , 112.32    ],
        [ 62.060997, 111.221   , 106.32    ],
        [ 57.060997, 104.221   ,  99.32    ]],

       [[ 79.061   , 134.22101 , 129.32    ],
        [ 79.061   , 134.22101 , 129.32    ],
        [ 79.061   , 134.22101 , 129.32    ],
        [ 78.061   , 132.22101 , 127.32    ],
        [ 76.061   , 130.22101 , 125.32    ],
        [ 73.061   , 126.221   , 121.32    ],
        [ 70.061   , 122.221   , 117.32    ],
        [ 67.061   , 118.221   , 112.32    ],
        [ 62.060997, 111.221   , 106.32    ],
        [ 57.060997, 104.221   ,  99.32    ]],

       [[ 79.061   , 134.22101 , 129.32    ],
        [ 79.061   , 134.22101 , 129.32    ],
        [ 79.061   , 134.22101 , 129.32    ],
        [ 78.061   , 132.22101 , 127.32    ],
        [ 76.061   , 130.22101 , 125.32    ],
        [ 73.061   , 126.221   , 121.32    ],
        [ 70.061   , 122.221   , 117.32    ],
        [ 67.061   , 118.221   , 112.32    ],
        [ 62.060997, 111.221   , 106.32    ],
        [ 57.060997, 104.221   ,  99.32    ]],

       [[ 79.061   , 134.22101 , 129.32    ],
        [ 79.061   , 134.22101 , 129.32    ],
        [ 79.061   , 134.22101 , 129.32    ],
        [ 78.061   , 132.22101 , 127.32    ],
        [ 76.061   , 130.22101 , 125.32    ],
        [ 73.061   , 126.221   , 121.32    ],
        [ 70.061   , 122.221   , 117.32    ],
        [ 67.061   , 118.221   , 112.32    ],
        [ 62.060997, 111.221   , 106.32    ],
        [ 57.060997, 104.221   ,  99.32    ]],

       [[ 78.061   , 134.22101 , 129.32    ],
        [ 78.061   , 134.22101 , 129.32    ],
        [ 78.061   , 134.22101 , 129.32    ],
        [ 77.061   , 132.22101 , 127.32    ],
        [ 75.061   , 130.22101 , 125.32    ],
        [ 72.061   , 126.221   , 121.32    ],
        [ 70.061   , 122.221   , 117.32    ],
        [ 66.061   , 118.221   , 112.32    ],
        [ 61.060997, 111.221   , 106.32    ],
        [ 56.060997, 104.221   ,  99.32    ]],

       [[ 78.061   , 134.22101 , 129.32    ],
        [ 78.061   , 134.22101 , 129.32    ],
        [ 78.061   , 134.22101 , 129.32    ],
        [ 77.061   , 132.22101 , 127.32    ],
        [ 75.061   , 130.22101 , 125.32    ],
        [ 72.061   , 126.221   , 121.32    ],
        [ 70.061   , 122.221   , 117.32    ],
        [ 66.061   , 118.221   , 112.32    ],
        [ 61.060997, 111.221   , 106.32    ],
        [ 56.060997, 104.221   ,  99.32    ]],

       [[ 78.061   , 134.22101 , 129.32    ],
        [ 78.061   , 134.22101 , 129.32    ],
        [ 78.061   , 134.22101 , 129.32    ],
        [ 77.061   , 132.22101 , 127.32    ],
        [ 75.061   , 130.22101 , 125.32    ],
        [ 72.061   , 126.221   , 121.32    ],
        [ 70.061   , 122.221   , 117.32    ],
        [ 66.061   , 118.221   , 112.32    ],
        [ 61.060997, 111.221   , 106.32    ],
        [ 56.060997, 104.221   ,  99.32    ]],

       [[ 78.061   , 134.22101 , 128.32    ],
        [ 78.061   , 134.22101 , 128.32    ],
        [ 78.061   , 134.22101 , 128.32    ],
        [ 77.061   , 132.22101 , 126.32    ],
        [ 75.061   , 130.22101 , 124.32    ],
        [ 72.061   , 126.221   , 120.32    ],
        [ 70.061   , 122.221   , 116.32    ],
        [ 66.061   , 118.221   , 111.32    ],
        [ 61.060997, 111.221   , 105.32    ],
        [ 56.060997, 104.221   ,  98.32    ]],

       [[ 78.061   , 134.22101 , 128.32    ],
        [ 78.061   , 134.22101 , 128.32    ],
        [ 78.061   , 134.22101 , 128.32    ],
        [ 77.061   , 132.22101 , 126.32    ],
        [ 75.061   , 130.22101 , 124.32    ],
        [ 72.061   , 126.221   , 120.32    ],
        [ 70.061   , 122.221   , 116.32    ],
        [ 66.061   , 118.221   , 111.32    ],
        [ 61.060997, 111.221   , 105.32    ],
        [ 56.060997, 104.221   ,  98.32    ]]], dtype=float32)
>>> 
============== RESTART: F:/Users/Administrator/Downloads/cr1.py ==============
>>> A[1:10,:10,:]
array([[[0.99215686, 0.9843137 , 0.7176471 ],
        [0.99215686, 0.9843137 , 0.7176471 ],
        [0.99215686, 0.9843137 , 0.7176471 ],
        [0.9843137 , 0.9764706 , 0.7137255 ],
        [0.9764706 , 0.96862745, 0.7058824 ],
        [0.9607843 , 0.9529412 , 0.69411767],
        [0.94509804, 0.9372549 , 0.68235296],
        [0.9254902 , 0.92156863, 0.67058825],
        [0.9019608 , 0.89411765, 0.6509804 ],
        [0.8745098 , 0.8666667 , 0.6313726 ]],

       [[0.99215686, 0.9843137 , 0.7176471 ],
        [0.99215686, 0.9843137 , 0.7176471 ],
        [0.99215686, 0.9843137 , 0.7176471 ],
        [0.9843137 , 0.9764706 , 0.7137255 ],
        [0.9764706 , 0.96862745, 0.7058824 ],
        [0.9607843 , 0.9529412 , 0.69411767],
        [0.94509804, 0.9372549 , 0.68235296],
        [0.9254902 , 0.92156863, 0.67058825],
        [0.9019608 , 0.89411765, 0.6509804 ],
        [0.8745098 , 0.8666667 , 0.6313726 ]],

       [[0.99215686, 0.9843137 , 0.7176471 ],
        [0.99215686, 0.9843137 , 0.7176471 ],
        [0.99215686, 0.9843137 , 0.7176471 ],
        [0.9843137 , 0.9764706 , 0.7137255 ],
        [0.9764706 , 0.96862745, 0.7058824 ],
        [0.9607843 , 0.9529412 , 0.69411767],
        [0.94509804, 0.9372549 , 0.68235296],
        [0.9254902 , 0.92156863, 0.67058825],
        [0.9019608 , 0.89411765, 0.6509804 ],
        [0.8745098 , 0.8666667 , 0.6313726 ]],

       [[0.99215686, 0.9843137 , 0.7176471 ],
        [0.99215686, 0.9843137 , 0.7176471 ],
        [0.99215686, 0.9843137 , 0.7176471 ],
        [0.9843137 , 0.9764706 , 0.7137255 ],
        [0.9764706 , 0.96862745, 0.7058824 ],
        [0.9607843 , 0.9529412 , 0.69411767],
        [0.94509804, 0.9372549 , 0.68235296],
        [0.9254902 , 0.92156863, 0.67058825],
        [0.9019608 , 0.89411765, 0.6509804 ],
        [0.8745098 , 0.8666667 , 0.6313726 ]],

       [[0.99215686, 0.9843137 , 0.7137255 ],
        [0.99215686, 0.9843137 , 0.7137255 ],
        [0.99215686, 0.9843137 , 0.7137255 ],
        [0.9843137 , 0.9764706 , 0.70980394],
        [0.9764706 , 0.96862745, 0.7019608 ],
        [0.9607843 , 0.9529412 , 0.6901961 ],
        [0.94509804, 0.9372549 , 0.68235296],
        [0.9254902 , 0.92156863, 0.6666667 ],
        [0.9019608 , 0.89411765, 0.64705884],
        [0.8745098 , 0.8666667 , 0.627451  ]],

       [[0.99215686, 0.9843137 , 0.7137255 ],
        [0.99215686, 0.9843137 , 0.7137255 ],
        [0.99215686, 0.9843137 , 0.7137255 ],
        [0.9843137 , 0.9764706 , 0.70980394],
        [0.9764706 , 0.96862745, 0.7019608 ],
        [0.9607843 , 0.9529412 , 0.6901961 ],
        [0.94509804, 0.9372549 , 0.68235296],
        [0.9254902 , 0.92156863, 0.6666667 ],
        [0.9019608 , 0.89411765, 0.64705884],
        [0.8745098 , 0.8666667 , 0.627451  ]],

       [[0.99215686, 0.9843137 , 0.7137255 ],
        [0.99215686, 0.9843137 , 0.7137255 ],
        [0.99215686, 0.9843137 , 0.7137255 ],
        [0.9843137 , 0.9764706 , 0.70980394],
        [0.9764706 , 0.96862745, 0.7019608 ],
        [0.9607843 , 0.9529412 , 0.6901961 ],
        [0.94509804, 0.9372549 , 0.68235296],
        [0.9254902 , 0.92156863, 0.6666667 ],
        [0.9019608 , 0.89411765, 0.64705884],
        [0.8745098 , 0.8666667 , 0.627451  ]],

       [[0.9882353 , 0.9843137 , 0.7137255 ],
        [0.9882353 , 0.9843137 , 0.7137255 ],
        [0.9882353 , 0.9843137 , 0.7137255 ],
        [0.98039216, 0.9764706 , 0.70980394],
        [0.972549  , 0.96862745, 0.7019608 ],
        [0.95686275, 0.9529412 , 0.6901961 ],
        [0.9411765 , 0.9372549 , 0.68235296],
        [0.92156863, 0.92156863, 0.6666667 ],
        [0.8980392 , 0.89411765, 0.64705884],
        [0.87058824, 0.8666667 , 0.627451  ]],

       [[0.9882353 , 0.9843137 , 0.7137255 ],
        [0.9882353 , 0.9843137 , 0.7137255 ],
        [0.9882353 , 0.9843137 , 0.7137255 ],
        [0.98039216, 0.9764706 , 0.70980394],
        [0.972549  , 0.96862745, 0.7019608 ],
        [0.95686275, 0.9529412 , 0.6901961 ],
        [0.9411765 , 0.9372549 , 0.68235296],
        [0.92156863, 0.92156863, 0.6666667 ],
        [0.8980392 , 0.89411765, 0.64705884],
        [0.87058824, 0.8666667 , 0.627451  ]]], dtype=float32)
>>> img.show(A)
>>> 
============== RESTART: F:/Users/Administrator/Downloads/cr1.py ==============
>>> img.show(A)
>>> # Run Region [9-11]
>>> img.show(A)
>>> A[1:10,:10,:]
array([[[1., 1., 1.],
        [1., 1., 1.],
        [1., 1., 1.],
        [1., 1., 1.],
        [1., 1., 1.],
        [1., 1., 1.],
        [1., 1., 1.],
        [1., 1., 1.],
        [1., 1., 1.],
        [1., 1., 1.]],

       [[1., 1., 1.],
        [1., 1., 1.],
        [1., 1., 1.],
        [1., 1., 1.],
        [1., 1., 1.],
        [1., 1., 1.],
        [1., 1., 1.],
        [1., 1., 1.],
        [1., 1., 1.],
        [1., 1., 1.]],

       [[1., 1., 1.],
        [1., 1., 1.],
        [1., 1., 1.],
        [1., 1., 1.],
        [1., 1., 1.],
        [1., 1., 1.],
        [1., 1., 1.],
        [1., 1., 1.],
        [1., 1., 1.],
        [1., 1., 1.]],

       [[1., 1., 1.],
        [1., 1., 1.],
        [1., 1., 1.],
        [1., 1., 1.],
        [1., 1., 1.],
        [1., 1., 1.],
        [1., 1., 1.],
        [1., 1., 1.],
        [1., 1., 1.],
        [1., 1., 1.]],

       [[1., 1., 1.],
        [1., 1., 1.],
        [1., 1., 1.],
        [1., 1., 1.],
        [1., 1., 1.],
        [1., 1., 1.],
        [1., 1., 1.],
        [1., 1., 1.],
        [1., 1., 1.],
        [1., 1., 1.]],

       [[1., 1., 1.],
        [1., 1., 1.],
        [1., 1., 1.],
        [1., 1., 1.],
        [1., 1., 1.],
        [1., 1., 1.],
        [1., 1., 1.],
        [1., 1., 1.],
        [1., 1., 1.],
        [1., 1., 1.]],

       [[1., 1., 1.],
        [1., 1., 1.],
        [1., 1., 1.],
        [1., 1., 1.],
        [1., 1., 1.],
        [1., 1., 1.],
        [1., 1., 1.],
        [1., 1., 1.],
        [1., 1., 1.],
        [1., 1., 1.]],

       [[1., 1., 1.],
        [1., 1., 1.],
        [1., 1., 1.],
        [1., 1., 1.],
        [1., 1., 1.],
        [1., 1., 1.],
        [1., 1., 1.],
        [1., 1., 1.],
        [1., 1., 1.],
        [1., 1., 1.]],

       [[1., 1., 1.],
        [1., 1., 1.],
        [1., 1., 1.],
        [1., 1., 1.],
        [1., 1., 1.],
        [1., 1., 1.],
        [1., 1., 1.],
        [1., 1., 1.],
        [1., 1., 1.],
        [1., 1., 1.]]], dtype=float32)
>>> np.where(A[1:10,:10,:]==0)
(array([], dtype=int64), array([], dtype=int64), array([], dtype=int64))
>>> np.where(A[1:10,:10,:]==[0, 0, 0])
(array([], dtype=int64), array([], dtype=int64), array([], dtype=int64))
>>> np.where(A[50,:10,:]==[0, 0, 0])
(array([], dtype=int64), array([], dtype=int64))
>>> np.where(A[50,:,:]==[0, 0, 0])
(array([ 94,  94,  94,  95,  95,  95,  96,  96,  96,  97,  97,  97,  98,
        98,  98,  99,  99,  99, 100, 100, 100, 101, 101, 101, 190, 190,
       190, 191, 191, 191, 192, 192, 192, 193, 193, 193, 194, 194, 194,
       195, 195, 195, 196, 196, 196, 197, 197, 197, 198, 198, 198, 199,
       199, 199, 377, 377, 377, 378, 378, 378, 379, 379, 379, 380, 380,
       380, 381, 381, 381, 501, 501, 501, 502, 502, 502, 503, 503, 503,
       504, 504, 504, 505, 505, 505, 506, 506, 506, 507, 507, 507, 671,
       671, 671, 672, 672, 672, 673, 673, 673, 674, 674, 674, 675, 675,
       675, 676, 676, 676, 677, 677, 677, 726, 726, 726, 727, 727, 727,
       728, 728, 728, 729, 729, 729, 730, 730, 730, 731, 731, 731, 732,
       732, 732, 913, 913, 913, 914, 914, 914, 915, 915, 915, 916, 916,
       916, 917, 917, 917, 918, 918, 918, 919, 919, 919], dtype=int64), array([0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0,
       1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1,
       2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2,
       0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0,
       1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1,
       2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2,
       0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2],
      dtype=int64))
>>> A[50,94,:]
array([0., 0., 0.], dtype=float32)
>>> A[50,95,:]
array([0., 0., 0.], dtype=float32)
>>> help(np.where)
Help on function where in module numpy:

where(...)
    where(condition, [x, y])
    
    Return elements chosen from `x` or `y` depending on `condition`.
    
    .. note::
        When only `condition` is provided, this function is a shorthand for
        ``np.asarray(condition).nonzero()``. Using `nonzero` directly should be
        preferred, as it behaves correctly for subclasses. The rest of this
        documentation covers only the case where all three arguments are
        provided.
    
    Parameters
    ----------
    condition : array_like, bool
        Where True, yield `x`, otherwise yield `y`.
    x, y : array_like
        Values from which to choose. `x`, `y` and `condition` need to be
        broadcastable to some shape.
    
    Returns
    -------
    out : ndarray
        An array with elements from `x` where `condition` is True, and elements
        from `y` elsewhere.
    
    See Also
    --------
    choose
    nonzero : The function that is called when x and y are omitted
    
    Notes
    -----
    If all the arrays are 1-D, `where` is equivalent to::
    
        [xv if c else yv
         for c, xv, yv in zip(condition, x, y)]
    
    Examples
    --------
    >>> a = np.arange(10)
    >>> a
    array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    >>> np.where(a < 5, a, 10*a)
    array([ 0,  1,  2,  3,  4, 50, 60, 70, 80, 90])
    
    This can be used on multidimensional arrays too:
    
    >>> np.where([[True, False], [True, True]],
    ...          [[1, 2], [3, 4]],
    ...          [[9, 8], [7, 6]])
    array([[1, 8],
           [3, 4]])
    
    The shapes of x, y, and the condition are broadcast together:
    
    >>> x, y = np.ogrid[:3, :4]
    >>> np.where(x < y, x, 10 + y)  # both x and 10+y are broadcast
    array([[10,  0,  0,  0],
           [10, 11,  1,  1],
           [10, 11, 12,  2]])
    
    >>> a = np.array([[0, 1, 2],
    ...               [0, 2, 4],
    ...               [0, 3, 6]])
    >>> np.where(a < 4, a, -1)  # -1 is broadcast
    array([[ 0,  1,  2],
           [ 0,  2, -1],
           [ 0,  3, -1]])

>>> np.where(A[50,:,:]==[0, 0, 0])
(array([ 94,  94,  94,  95,  95,  95,  96,  96,  96,  97,  97,  97,  98,
        98,  98,  99,  99,  99, 100, 100, 100, 101, 101, 101, 190, 190,
       190, 191, 191, 191, 192, 192, 192, 193, 193, 193, 194, 194, 194,
       195, 195, 195, 196, 196, 196, 197, 197, 197, 198, 198, 198, 199,
       199, 199, 377, 377, 377, 378, 378, 378, 379, 379, 379, 380, 380,
       380, 381, 381, 381, 501, 501, 501, 502, 502, 502, 503, 503, 503,
       504, 504, 504, 505, 505, 505, 506, 506, 506, 507, 507, 507, 671,
       671, 671, 672, 672, 672, 673, 673, 673, 674, 674, 674, 675, 675,
       675, 676, 676, 676, 677, 677, 677, 726, 726, 726, 727, 727, 727,
       728, 728, 728, 729, 729, 729, 730, 730, 730, 731, 731, 731, 732,
       732, 732, 913, 913, 913, 914, 914, 914, 915, 915, 915, 916, 916,
       916, 917, 917, 917, 918, 918, 918, 919, 919, 919], dtype=int64), array([0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0,
       1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1,
       2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2,
       0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0,
       1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1,
       2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2,
       0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2],
      dtype=int64))
>>> A[50,95,:]
array([0., 0., 0.], dtype=float32)
>>> sum(A[50,95,:])
0.0
>>> np.where(sum(A[50,:,:])==[0, 0, 0])
(array([], dtype=int64),)
>>> np.where(sum(A[50,:,:])==0)
(array([], dtype=int64),)
>>> np.where(sum(A[50,:,:])==0.)
(array([], dtype=int64),)
>>> sum(A[50,:,:])
array([1064., 1064., 1064.], dtype=float32)
>>> A1 = [sum(A[50,m:m+1,:]) for m in range(600)]
>>> np.where(A1==0)
(array([], dtype=int64),)
>>> A1

>>> A1[94]
array([0., 0., 0.], dtype=float32)
>>> np.where(sum(A1)==0)
(array([], dtype=int64),)
>>> np.where(sum(A1)<1e-16)
(array([], dtype=int64),)
>>> np.where(sum(A1[:])<1e-16)
(array([], dtype=int64),)
>>> A1[1:10]
[array([1., 1., 1.], dtype=float32), array([1., 1., 1.], dtype=float32), array([1., 1., 1.], dtype=float32), array([1., 1., 1.], dtype=float32), array([1., 1., 1.], dtype=float32), array([1., 1., 1.], dtype=float32), array([1., 1., 1.], dtype=float32), array([1., 1., 1.], dtype=float32), array([1., 1., 1.], dtype=float32)]
>>> [sum(A[50,m:m+1,:]) for m in range(6)]
[array([1., 1., 1.], dtype=float32), array([1., 1., 1.], dtype=float32), array([1., 1., 1.], dtype=float32), array([1., 1., 1.], dtype=float32), array([1., 1., 1.], dtype=float32), array([1., 1., 1.], dtype=float32)]
>>> [sum(A[50,m:m+1,:][0]) for m in range(6)]
[3.0, 3.0, 3.0, 3.0, 3.0, 3.0]
>>> [sum(A[50,m:m+1,:][0]) for m in range(90,100)]
[3.0, 3.0, 3.0, 3.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
>>> A1= [sum(A[50,m:m+1,:][0]) for m in range(600)]
>>> np.where(A1==0)
(array([], dtype=int64),)
>>> A1[1:10]
[3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0]
>>> A1[90:100]
[3.0, 3.0, 3.0, 3.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
>>> np.where(A1<1e-16)
Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    np.where(A1<1e-16)
TypeError: '<' not supported between instances of 'list' and 'float'
>>> np.where(np.array(A1)<1e-16)
(array([ 94,  95,  96,  97,  98,  99, 100, 101, 190, 191, 192, 193, 194,
       195, 196, 197, 198, 199, 377, 378, 379, 380, 381, 501, 502, 503,
       504, 505, 506, 507], dtype=int64),)
>>> img.show()
>>> import matplotlib.pylab as plt
>>> plt.imshow(img)
<matplotlib.image.AxesImage object at 0x0000000016E20070>
>>> plt.plot(range(0,600),350)
Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    plt.plot(range(0,600),350)
  File "F:\Anaconda3\envs\deepxde\lib\site-packages\matplotlib\pyplot.py", line 3019, in plot
    return gca().plot(
  File "F:\Anaconda3\envs\deepxde\lib\site-packages\matplotlib\axes\_axes.py", line 1605, in plot
    lines = [*self._get_lines(*args, data=data, **kwargs)]
  File "F:\Anaconda3\envs\deepxde\lib\site-packages\matplotlib\axes\_base.py", line 315, in __call__
    yield from self._plot_args(this, kwargs)
  File "F:\Anaconda3\envs\deepxde\lib\site-packages\matplotlib\axes\_base.py", line 501, in _plot_args
    raise ValueError(f"x and y must have same first dimension, but "
ValueError: x and y must have same first dimension, but have shapes (600,) and (1,)
>>> plt.plot(range(0,600),350*range(0,600))
Traceback (most recent call last):
  File "<pyshell#100>", line 1, in <module>
    plt.plot(range(0,600),350*range(0,600))
TypeError: unsupported operand type(s) for *: 'int' and 'range'
>>> plt.plot(range(0,600),350*np.array(range(0,600)))
[<matplotlib.lines.Line2D object at 0x0000000016E208E0>]
>>> plt.show()
>>> plt.imshow(img)
<matplotlib.image.AxesImage object at 0x000000001A05E640>
>>> plt.show()
>>> np.where(np.array(A1)<1e-16)
(array([ 94,  95,  96,  97,  98,  99, 100, 101, 190, 191, 192, 193, 194,
       195, 196, 197, 198, 199, 377, 378, 379, 380, 381, 501, 502, 503,
       504, 505, 506, 507], dtype=int64),)
>>> plt.plot(A1);plt.show()
[<matplotlib.lines.Line2D object at 0x000000001A0CA520>]
>>> A.shape
(600, 1115, 3)
>>> A1= [sum(A[50,m:m+1,:][0]) for m in range(A.shape[1])]
>>> plt.plot(A1);plt.show()
[<matplotlib.lines.Line2D object at 0x000000001813DC70>]

    There is an error (invalid syntax) at line 16, column 8.
>>> 
>>> 
============== RESTART: F:/Users/Administrator/Downloads/cr1.py ==============
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr1.py", line 18, in <module>
    Pix.update({irow:ODixt()})
NameError: name 'ODixt' is not defined
>>> # Run Region [18-20]
Traceback (most recent call last):
  File "<string>", line 20, in <module>
TypeError: '<' not supported between instances of 'list' and 'float'
>>> Pix
OrderedDict([(50, OrderedDict())])
>>> Pix[50]
OrderedDict()
>>> Pix[50].update({'blacks':0})
>>> # Run Region [line 20]
Traceback (most recent call last):
  File "<string>", line 20, in <module>
TypeError: '<' not supported between instances of 'list' and 'float'
>>> # Run Region [line 20]
Traceback (most recent call last):
  File "<string>", line 20, in <module>
TypeError: '<' not supported between instances of 'list' and 'float'
>>> # Run Region [line 20]
Traceback (most recent call last):
  File "<string>", line 20, in <module>
TypeError: '<' not supported between instances of 'list' and 'float'
>>> np.where(A1<EPS)
Traceback (most recent call last):
  File "<pyshell#113>", line 1, in <module>
    np.where(A1<EPS)
TypeError: '<' not supported between instances of 'list' and 'float'
>>> type(A1)
<class 'list'>
>>> # Run Region [19-20]
>>> Pix
OrderedDict([(50, OrderedDict([('blacks', (array([ 94,  95,  96,  97,  98,  99, 100, 101, 190, 191, 192, 193, 194,
       195, 196, 197, 198, 199, 377, 378, 379, 380, 381, 501, 502, 503,
       504, 505, 506, 507, 671, 672, 673, 674, 675, 676, 677, 726, 727,
       728, 729, 730, 731, 732, 913, 914, 915, 916, 917, 918, 919],
      dtype=int64),))]))])
>>> # Run Region [23-42]
>>> pix1 = pix_extract_sets(Pix)
Traceback (most recent call last):
  File "<pyshell#116>", line 1, in <module>
    pix1 = pix_extract_sets(Pix)
  File "<string>", line 26, in pix_extract_sets
TypeError: 'int' object is not iterable
>>> len(Pix.keys())
1
>>> # Run Region [23-43]
>>> pix1 = pix_extract_sets(Pix)
Traceback (most recent call last):
  File "<pyshell#118>", line 1, in <module>
    pix1 = pix_extract_sets(Pix)
  File "<string>", line 34, in pix_extract_sets
UnboundLocalError: local variable 'icol' referenced before assignment
>>> # Run Region [23-43]
>>> pix1 = pix_extract_sets(Pix)
Traceback (most recent call last):
  File "<pyshell#119>", line 1, in <module>
    pix1 = pix_extract_sets(Pix)
  File "<string>", line 35, in pix_extract_sets
NameError: name 'nBlacks' is not defined
>>> # Run Region [23-43]
>>> pix1 = pix_extract_sets(Pix)
Traceback (most recent call last):
  File "<pyshell#120>", line 1, in <module>
    pix1 = pix_extract_sets(Pix)
  File "<string>", line 35, in pix_extract_sets
ValueError: The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()
>>> 
============== RESTART: F:/Users/Administrator/Downloads/cr1.py ==============
>>> Set
OrderedDict([(0, [array([ 94,  95,  96,  97,  98,  99, 100, 101, 190, 191, 192, 193, 194,
       195, 196, 197, 198, 199, 377, 378, 379, 380, 381, 501, 502, 503,
       504, 505, 506, 507, 671, 672, 673, 674, 675, 676, 677, 726, 727,
       728, 729, 730, 731, 732, 913, 914, 915, 916, 917, 918, 919],
      dtype=int64)])])
>>> pix1= Pix
>>> rows = pix1.keys()
>>> rows
odict_keys([50])
>>> irow = rows[0]
Traceback (most recent call last):
  File "<pyshell#125>", line 1, in <module>
    irow = rows[0]
TypeError: 'odict_keys' object is not subscriptable
>>> rows = list(pix1.keys())
>>> irow = rows[0]
>>> irow
50
>>> iSet= 0
>>> Set= ODict()
>>> blacks = pix1[irow]['blacks']
>>> blacks
(array([ 94,  95,  96,  97,  98,  99, 100, 101, 190, 191, 192, 193, 194,
       195, 196, 197, 198, 199, 377, 378, 379, 380, 381, 501, 502, 503,
       504, 505, 506, 507, 671, 672, 673, 674, 675, 676, 677, 726, 727,
       728, 729, 730, 731, 732, 913, 914, 915, 916, 917, 918, 919],
      dtype=int64),)
>>> nBlacks = len(blacks)
>>> nBlacks
1
>>> pix1[irow]['blacks'][0]
array([ 94,  95,  96,  97,  98,  99, 100, 101, 190, 191, 192, 193, 194,
       195, 196, 197, 198, 199, 377, 378, 379, 380, 381, 501, 502, 503,
       504, 505, 506, 507, 671, 672, 673, 674, 675, 676, 677, 726, 727,
       728, 729, 730, 731, 732, 913, 914, 915, 916, 917, 918, 919],
      dtype=int64)
>>> list(pix1[irow]['blacks'][0])
[94, 95, 96, 97, 98, 99, 100, 101, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 377, 378, 379, 380, 381, 501, 502, 503, 504, 505, 506, 507, 671, 672, 673, 674, 675, 676, 677, 726, 727, 728, 729, 730, 731, 732, 913, 914, 915, 916, 917, 918, 919]
>>> blacks  = list(pix1[irow]['blacks'][0])
>>> # Run Region [17-20]
>>> # Run Region [line 25]
>>> # Run Region [line 33]
>>> blacks
[94, 95, 96, 97, 98, 99, 100, 101, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 377, 378, 379, 380, 381, 501, 502, 503, 504, 505, 506, 507, 671, 672, 673, 674, 675, 676, 677, 726, 727, 728, 729, 730, 731, 732, 913, 914, 915, 916, 917, 918, 919]
>>> nBlacks
1
>>> nBlacks = len(blacks)
>>> nBlacks
51
>>> Set[iSet] = blacks[0]
>>> Set
OrderedDict([(0, 94)])
>>> # Run Region [line 35]
>>> Set
OrderedDict([(0, [94])])
>>> Set[0]
[94]
>>> iblack=1
>>> blacks[iblack]
95
>>> blacks[iblack]-Set[iSet]==1
array([ True])
>>> if(blacks[iblack]-Set[iSet]==1):
	1

	
1
>>> Set[iSet].append(iblack# Run Region [line 38]
>>> iblack
1
>>> # Run Region [39-43]
>>> Set
OrderedDict([(0, [94, 95])])
>>> # Run Region [24-45]
Traceback (most recent call last):
  File "<string>", line 28, in <module>
NameError: name 'listr' is not defined
>>> # Run Region [24-45]
>>> pix1
OrderedDict([(50, OrderedDict([('blacks', [94, 95, 96, 97, 98, 99, 100, 101, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 377, 378, 379, 380, 381, 501, 502, 503, 504, 505, 506, 507, 671, 672, 673, 674, 675, 676, 677, 726, 727, 728, 729, 730, 731, 732, 913, 914, 915, 916, 917, 918, 919]), ('sets', OrderedDict([(0, [94, 95, 96, 97, 98, 99, 100, 101]), (1, [8]), (2, [9]), (3, [10]), (4, [11]), (5, [12]), (6, [13]), (7, [14]), (8, [15]), (9, [16]), (10, [17]), (11, [18]), (12, [19]), (13, [20]), (14, [21]), (15, [22]), (16, [23]), (17, [24]), (18, [25]), (19, [26]), (20, [27]), (21, [28]), (22, [29]), (23, [30]), (24, [31]), (25, [32]), (26, [33]), (27, [34]), (28, [35]), (29, [36]), (30, [37]), (31, [38]), (32, [39]), (33, [40]), (34, [41]), (35, [42]), (36, [43]), (37, [44]), (38, [45]), (39, [46]), (40, [47]), (41, [48]), (42, [49]), (43, [50])]))]))])
>>> iblack
51
>>> iblack=8
>>> blacks[iblack]
190
>>> # Run Region [24-45]
>>> pix1[50]['sets']
OrderedDict([(0, [94, 95, 96, 97, 98, 99, 100, 101]), (1, [190, 191, 192, 193, 194, 195, 196, 197, 198, 199]), (2, [377, 378, 379, 380, 381]), (3, [501, 502, 503, 504, 505, 506, 507]), (4, [671, 672, 673, 674, 675, 676, 677]), (5, [726, 727, 728, 729, 730, 731, 732]), (6, [913, 914, 915, 916, 917, 918, 919])])
>>> 
============== RESTART: F:/Users/Administrator/Downloads/cr1.py ==============
>>> # Run Region [19-22]
>>> pix2 = pix_extract_sets(Pix)
Traceback (most recent call last):
  File "<pyshell#159>", line 1, in <module>
    pix2 = pix_extract_sets(Pix)
  File "F:/Users/Administrator/Downloads/cr1.py", line 32, in pix_extract_sets
    Set[iSet] = [blacks[0]]
IndexError: list index out of range
>>> # Run Region [25-48]
>>> pix2 = pix_extract_sets(Pix)
>>> pix2[40]['sets']
OrderedDict([(0, [102, 103, 104, 105, 106, 107, 108, 109, 110]), (1, [183, 184, 185, 186, 187, 188, 189, 190, 191]), (2, [501, 502, 503, 504, 505, 506, 507]), (3, [671, 672, 673, 674, 675, 676, 677]), (4, [726, 727, 728, 729, 730, 731, 732]), (5, [913, 914, 915, 916, 917, 918, 919])])
>>> pix2[41]['sets']
OrderedDict([(0, [101, 102, 103, 104, 105, 106, 107, 108]), (1, [184, 185, 186, 187, 188, 189, 190, 191, 192]), (2, [501, 502, 503, 504, 505, 506, 507]), (3, [671, 672, 673, 674, 675, 676, 677]), (4, [726, 727, 728, 729, 730, 731, 732]), (5, [913, 914, 915, 916, 917, 918, 919])])
>>> 
============== RESTART: F:/Users/Administrator/Downloads/cr1.py ==============
>>> pix2[0]['sets']
Traceback (most recent call last):
  File "<pyshell#163>", line 1, in <module>
    pix2[0]['sets']
NameError: name 'pix2' is not defined
>>> Pix1[0]['sets']
[]
>>> 
============== RESTART: F:/Users/Administrator/Downloads/cr1.py ==============
>>> Pix1[0]['sets']
[]
>>> Pix1[41]['sets']
[]
>>> Pix1[51]['sets']
[]
>>> Pix1

>>> Pix1[51]
OrderedDict([('blacks', [92, 93, 94, 95, 96, 97, 98, 99, 100, 192, 193, 194, 195, 196, 197, 198, 199, 376, 377, 378, 379, 380, 381, 382, 501, 502, 503, 504, 505, 506, 507, 671, 672, 673, 674, 675, 676, 677, 726, 727, 728, 729, 730, 731, 732, 913, 914, 915, 916, 917, 918, 919]), ('sets', [])])
>>> # Run Region [28-52]
>>> rows
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347, 348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365, 366, 367, 368, 369, 370, 371, 372, 373, 374, 375, 376, 377, 378, 379, 380, 381, 382, 383, 384, 385, 386, 387, 388, 389, 390, 391, 392, 393, 394, 395, 396, 397, 398, 399, 400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 419, 420, 421, 422, 423, 424, 425, 426, 427, 428, 429, 430, 431, 432, 433, 434, 435, 436, 437, 438, 439, 440, 441, 442, 443, 444, 445, 446, 447, 448, 449, 450, 451, 452, 453, 454, 455, 456, 457, 458, 459, 460, 461, 462, 463, 464, 465, 466, 467, 468, 469, 470, 471, 472, 473, 474, 475, 476, 477, 478, 479, 480, 481, 482, 483, 484, 485, 486, 487, 488, 489, 490, 491, 492, 493, 494, 495, 496, 497, 498, 499, 500, 501, 502, 503, 504, 505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515, 516, 517, 518, 519, 520, 521, 522, 523, 524, 525, 526, 527, 528, 529, 530, 531, 532, 533, 534, 535, 536, 537, 538, 539, 540, 541, 542, 543, 544, 545, 546, 547, 548, 549, 550, 551, 552, 553, 554, 555, 556, 557, 558, 559, 560, 561, 562, 563, 564, 565, 566, 567, 568, 569, 570, 571, 572, 573, 574, 575, 576, 577, 578, 579, 580, 581, 582, 583, 584, 585, 586, 587, 588, 589, 590, 591, 592, 593, 594, 595, 596, 597, 598, 599]
>>> iSet = 0
>>> Set = ODict()
>>> irow= 0; blacks = pix1[irow]['blacks']
>>> blacks
[]
>>> irow= 50; blacks = pix1[irow]['blacks']
>>> blacks
[94, 95, 96, 97, 98, 99, 100, 101, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 377, 378, 379, 380, 381, 501, 502, 503, 504, 505, 506, 507, 671, 672, 673, 674, 675, 676, 677, 726, 727, 728, 729, 730, 731, 732, 913, 914, 915, 916, 917, 918, 919]
>>> nBlacks = len(blacks)
>>> Set[iSet] = ODict({'begin':blacks[0]})
>>> Set
OrderedDict([(0, OrderedDict([('begin', 94)]))])
>>> iblack =1
>>> # Run Region [37-51]
Traceback (most recent call last):
  File "<string>", line 44, in <module>
KeyError: -1
>>> # Run Region [35-53]
Traceback (most recent call last):
  File "<string>", line 45, in <module>
TypeError: list indices must be integers or slices, not str
>>> black
191
>>> Set
OrderedDict([(0, OrderedDict([('list', [94, 95, 96, 97, 98, 99, 100, 101]), ('end', 101)])), (1, [190])])
>>> iblack
9
>>> # Run Region [29-55]
Traceback (most recent call last):
  File "<string>", line 45, in <module>
KeyError: 'list'
>>> # Run Region [29-55]
>>> Pix1[51]
OrderedDict([('blacks', [92, 93, 94, 95, 96, 97, 98, 99, 100, 192, 193, 194, 195, 196, 197, 198, 199, 376, 377, 378, 379, 380, 381, 382, 501, 502, 503, 504, 505, 506, 507, 671, 672, 673, 674, 675, 676, 677, 726, 727, 728, 729, 730, 731, 732, 913, 914, 915, 916, 917, 918, 919]), ('sets', OrderedDict([(0, OrderedDict([('begin', 92), ('list', [92, 93, 94, 95, 96, 97, 98, 99, 100]), ('end', 100)])), (1, OrderedDict([('begin', 192), ('list', [192, 193, 194, 195, 196, 197, 198, 199]), ('end', 199)])), (2, OrderedDict([('begin', 376), ('list', [376, 377, 378, 379, 380, 381, 382]), ('end', 382)])), (3, OrderedDict([('begin', 501), ('list', [501, 502, 503, 504, 505, 506, 507]), ('end', 507)])), (4, OrderedDict([('begin', 671), ('list', [671, 672, 673, 674, 675, 676, 677]), ('end', 677)])), (5, OrderedDict([('begin', 726), ('list', [726, 727, 728, 729, 730, 731, 732]), ('end', 732)])), (6, OrderedDict([('begin', 913), ('list', [913, 914, 915, 916, 917, 918, 919]), ('end', 919)]))]))])
>>> Pix1[51]['sets'][1]['begin']
192
>>> Pix1[51]['sets'][1]['end']
199
>>> # Run Region [28-56]
>>> Pix1[51]['sets'][1]['end']
199
>>> Pix1[51]['sets'][1]['count']
8
>>> 
============== RESTART: F:/Users/Administrator/Downloads/cr1.py ==============
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr1.py", line 63, in <module>
    Pix1 = pix_extract_sets(Pix1)
NameError: name 'pix_extract_sets' is not defined
>>> # Run Region [line 63]
>>> Pix1[51]['rowsets'][1]['count']
8
>>> 
    There is an error (invalid syntax) at line 72, column 16.
>>> # Run Region [68-69]
Traceback (most recent call last):
  File "<string>", line 68, in <module>
NameError: name 'pix' is not defined
>>> # Run Region [line 62]
>>> # Run Region [68-69]
Traceback (most recent call last):
  File "<string>", line 68, in <module>
NameError: name 'rowCount' is not defined
>>> # Run Region [67-69]
Traceback (most recent call last):
  File "<string>", line 68, in <module>
TypeError: '<' not supported between instances of 'list' and 'int'
>>> pix[rowCount]['rowsets']['count']
Traceback (most recent call last):
  File "<pyshell#190>", line 1, in <module>
    pix[rowCount]['rowsets']['count']
TypeError: list indices must be integers or slices, not str
>>> pix[rowCount]['rowsets']
[]
>>> len(pix[rowCount]['rowsets'])
0
>>> # Run Region [67-69]
>>> rowCount
21
>>> # Run Region [31-58]
Traceback (most recent call last):
** IDLE Internal Exception: 
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 351, in runcode
    exec(code, self.locals)
  File "<string>", line 58
SyntaxError: 'return' outside function
>>> # Run Region [27-55]
>>> # Run Region [line 77]
Traceback (most recent call last):
  File "<string>", line 77, in <module>
  File "<string>", line 54, in pix_extract_rowsets
AttributeError: 'list' object has no attribute 'keys'
>>> Set
Traceback (most recent call last):
  File "<pyshell#194>", line 1, in <module>
    Set
NameError: name 'Set' is not defined
>>> # Run Region [28-57]
Traceback (most recent call last):
  File "<string>", line 57, in <module>
AttributeError: 'list' object has no attribute 'keys'
>>> Set
[]
>>> 
    There is an error (expected an indented block) at line 56, column 9.
>>> # Run Region [28-58]
>>> pix1[21]['num_rowsets']
1
>>> pix1[51]['num_rowsets']
7
>>> 
============== RESTART: F:/Users/Administrator/Downloads/cr1.py ==============
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr1.py", line 64, in <module>
    pix = Pix1
NameError: name 'Pix1' is not defined
>>> # Run Region [80-81]
>>> # Run Region [64-67]
>>> # Run Region [63-74]
Traceback (most recent call last):
  File "<string>", line 74, in <module>
TypeError: tuple expected at most 1 argument, got 2
>>> # Run Region [63-74]
Traceback (most recent call last):
  File "<string>", line 74, in <module>
KeyError: 0
>>> # Run Region [63-74]
Traceback (most recent call last):
  File "<string>", line 74, in <module>
NameError: name 'ODICT' is not defined
>>> # Run Region [63-74]
>>> vertices
OrderedDict([(0, OrderedDict([('start', (538, 0))]))])
>>> irow
599
>>> # Run Region [64-75]
>>> vertices
OrderedDict([(0, OrderedDict([('start', (21, 0))]))])
>>> Pix1[25]['num_sets']
Traceback (most recent call last):
  File "<pyshell#201>", line 1, in <module>
    Pix1[25]['num_sets']
KeyError: 'num_sets'
>>> Pix1[25]['num_rowsets']
3
>>> Pix1[26]['num_rowsets']
5
>>> Pix1[26]['rowsets'][3]
OrderedDict([('begin', 501), ('list', [501, 502, 503, 504, 505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515, 516, 517, 518, 519, 520, 521, 522, 523, 524, 525, 526, 527, 528, 529, 530, 531, 532, 533, 534, 535, 536, 537, 538, 539, 540, 541, 542, 543, 544, 545, 546, 547, 548, 549, 550, 551, 552, 553, 554, 555, 556, 557, 558, 559, 560, 561, 562, 563, 564, 565, 566, 567, 568, 569, 570, 571, 572, 573, 574, 575, 576, 577, 578, 579, 580, 581, 582, 583, 584, 585, 586, 587, 588, 589, 590, 591, 592, 593, 594, 595, 596, 597, 598, 599, 600, 601, 602, 603, 604, 605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 616, 617, 618, 619, 620, 621, 622, 623, 624, 625, 626, 627, 628, 629, 630, 631, 632, 633, 634, 635, 636, 637, 638, 639, 640, 641, 642, 643, 644, 645, 646, 647, 648, 649, 650, 651, 652, 653, 654, 655, 656, 657, 658, 659, 660, 661, 662, 663, 664, 665, 666, 667, 668, 669, 670, 671, 672, 673, 674, 675, 676, 677]), ('end', 677), ('count', 177)])
>>> Pix1[27]['rowsets'][3]
OrderedDict([('begin', 501), ('list', [501, 502, 503, 504, 505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515, 516, 517, 518, 519, 520, 521, 522, 523, 524, 525, 526, 527, 528, 529, 530, 531, 532, 533, 534, 535, 536, 537, 538, 539, 540, 541, 542, 543, 544, 545, 546, 547, 548, 549, 550, 551, 552, 553, 554, 555, 556, 557, 558, 559, 560, 561, 562, 563, 564, 565, 566, 567, 568, 569, 570, 571, 572, 573, 574, 575, 576, 577, 578, 579, 580, 581, 582, 583, 584, 585, 586, 587, 588, 589, 590, 591, 592, 593, 594, 595, 596, 597, 598, 599, 600, 601, 602, 603, 604, 605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 616, 617, 618, 619, 620, 621, 622, 623, 624, 625, 626, 627, 628, 629, 630, 631, 632, 633, 634, 635, 636, 637, 638, 639, 640, 641, 642, 643, 644, 645, 646, 647, 648, 649, 650, 651, 652, 653, 654, 655, 656, 657, 658, 659, 660, 661, 662, 663, 664, 665, 666, 667, 668, 669, 670, 671, 672, 673, 674, 675, 676, 677]), ('end', 677), ('count', 177)])
>>> (22.5-15)/15
0.5
>>> import cv2
>>> 0.6*40
24.0
>>> 0.3*40
12.0
>>> 0.3*44
13.2
>>> 0.56*40
22.400000000000002
>>> 0.3*40
12.0
>>> 3./18
0.16666666666666666
>>> import cv2
>>> import matplotlib.pylab as pylab
>>> import os
>>> os.getcwd()
'F:\\Users\\Administrator\\Downloads'
>>> video= cv2.VideoCapture('mixkit-white-sand-beach-and-palm-trees-1564-large.mp4')
>>> help(video)

>>> while (true):
	ret, frame= video.read()
	imgFrame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
	pylab.imshow(imgFrame)
	pylab.show()

	
Traceback (most recent call last):
  File "<pyshell#225>", line 1, in <module>
    while (true):
NameError: name 'true' is not defined
>>> while (True):
	ret, frame= video.read()
	imgFrame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
	pylab.imshow(imgFrame)
	pylab.show()

	
<matplotlib.image.AxesImage object at 0x00000000199EF970>
<matplotlib.image.AxesImage object at 0x000000001AC37A00>
<matplotlib.image.AxesImage object at 0x000000001ADD6790>
<matplotlib.image.AxesImage object at 0x000000001AB0D400>
<matplotlib.image.AxesImage object at 0x000000001AB819A0>
<matplotlib.image.AxesImage object at 0x000000001ABEAFD0>
<matplotlib.image.AxesImage object at 0x000000001ABA2EB0>
<matplotlib.image.AxesImage object at 0x0000000019A9A310>
<matplotlib.image.AxesImage object at 0x000000001ADE7FD0>
<matplotlib.image.AxesImage object at 0x000000001AB3E670>

=============================== RESTART: Shell ===============================
>>> 
KeyboardInterrupt
>>> while (True):
	ret, frame= video.read()
	imgFrame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
	pylab.imshow(imgFrame)
	pylab.show()
	pylab.pause(0.3)
	pylab.close()

	
Traceback (most recent call last):
  File "<pyshell#231>", line 2, in <module>
    ret, frame= video.read()
NameError: name 'video' is not defined
>>> video= cv2.VideoCapture('mixkit-white-sand-beach-and-palm-trees-1564-large.mp4')
Traceback (most recent call last):
  File "<pyshell#232>", line 1, in <module>
    video= cv2.VideoCapture('mixkit-white-sand-beach-and-palm-trees-1564-large.mp4')
NameError: name 'cv2' is not defined
>>> import cv2
>>> import matplotlib.pylab as pylab
>>> video= cv2.VideoCapture('mixkit-white-sand-beach-and-palm-trees-1564-large.mp4')
>>> while (True):
	ret, frame= video.read()
	imgFrame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
	pylab.imshow(imgFrame)
	pylab.show()
	pylab.pause(0.3)
	pylab.close()

	
Traceback (most recent call last):
  File "<pyshell#237>", line 3, in <module>
    imgFrame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\imgproc\src\color.cpp:181: error: (-215:Assertion failed) !_src.empty() in function 'cv::cvtColor'

>>> 
============== RESTART: F:/Users/Administrator/Downloads/cr2.py ==============

=============================== RESTART: Shell ===============================
>>> 
============== RESTART: F:/Users/Administrator/Downloads/cr2.py ==============

=============================== RESTART: Shell ===============================
>>> 
============== RESTART: F:/Users/Administrator/Downloads/cr2.py ==============

=============================== RESTART: Shell ===============================
>>> 
============== RESTART: F:/Users/Administrator/Downloads/cr2.py ==============

=============================== RESTART: Shell ===============================
>>> 
============== RESTART: F:/Users/Administrator/Downloads/cr2.py ==============

=============================== RESTART: Shell ===============================
>>> 
=============================== RESTART: Shell ===============================
>>> 
============== RESTART: F:/Users/Administrator/Downloads/cr2.py ==============
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr2.py", line 12, in <module>
    time.sleep(0.2)
AttributeError: 'builtin_function_or_method' object has no attribute 'sleep'
>>> 
============== RESTART: F:/Users/Administrator/Downloads/cr2.py ==============

=============================== RESTART: Shell ===============================
>>> 
============== RESTART: F:/Users/Administrator/Downloads/cr2.py ==============

=============================== RESTART: Shell ===============================
>>> 
============== RESTART: F:/Users/Administrator/Downloads/cr2.py ==============

=============================== RESTART: Shell ===============================
>>> 
============== RESTART: F:/Users/Administrator/Downloads/cr2.py ==============

=============================== RESTART: Shell ===============================
>>> 
============== RESTART: F:/Users/Administrator/Downloads/cr2.py ==============

=============================== RESTART: Shell ===============================
>>> import matplotlib.pylab as pylab
>>> help(pylab.pause)
Help on function pause in module matplotlib.pyplot:

pause(interval)
    Run the GUI event loop for *interval* seconds.
    
    If there is an active figure, it will be updated and displayed before the
    pause, and the GUI event loop (if any) will run during the pause.
    
    This can be used for crude animation.  For more complex animation use
    :mod:`matplotlib.animation`.
    
    If there is no active figure, sleep for *interval* seconds instead.
    
    See Also
    --------
    matplotlib.animation : Proper animations
    show : Show all figures and optional block until all figures are closed.

>>> 
============== RESTART: F:/Users/Administrator/Downloads/cr2.py ==============

=============================== RESTART: Shell ===============================
>>> # Run Region [1-3]
>>> 
============== RESTART: F:/Users/Administrator/Downloads/cr2.py ==============

=============================== RESTART: Shell ===============================
>>> 
============== RESTART: F:/Users/Administrator/Downloads/cr2.py ==============

=============================== RESTART: Shell ===============================
>>> 
============== RESTART: F:/Users/Administrator/Downloads/cr2.py ==============

=============================== RESTART: Shell ===============================
>>> 
============== RESTART: F:/Users/Administrator/Downloads/cr2.py ==============

=============================== RESTART: Shell ===============================
>>> # Run Region [line 14]
Traceback (most recent call last):
  File "<string>", line 14, in <module>
NameError: name 'plt' is not defined
>>> 
 RESTART: F:/Users/Administrator/Downloads/chapter01-introduction-image-load-show-save.py 
>>> 
 RESTART: F:/Users/Administrator/Downloads/chapter01-introduction-image-load-show-save.py 
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/chapter01-introduction-image-load-show-save.py", line 10, in <module>
    plt.pause()
TypeError: pause() missing 1 required positional argument: 'interval'
>>> 
 RESTART: F:/Users/Administrator/Downloads/chapter01-introduction-image-load-show-save.py 
>>> 
 RESTART: F:/Users/Administrator/Downloads/chapter01-introduction-image-load-show-save.py 
>>> 
 RESTART: F:/Users/Administrator/Downloads/chapter01-introduction-image-load-show-save.py 
>>> 
 RESTART: F:/Users/Administrator/Downloads/chapter01-introduction-image-load-show-save.py 
>>> # Run Region [20-24]
>>> 
============== RESTART: F:/Users/Administrator/Downloads/cr2.py ==============

=============================== RESTART: Shell ===============================
>>> 
============== RESTART: F:/Users/Administrator/Downloads/cr2.py ==============
>>> 
============== RESTART: F:/Users/Administrator/Downloads/cr2.py ==============
>>> cv2.imshow(frame)
Traceback (most recent call last):
  File "<pyshell#240>", line 1, in <module>
    cv2.imshow(frame)
TypeError: imshow() missing required argument 'mat' (pos 2)
>>> cv2.imshow('1',frame)
>>> video.retrieve()
(True, array([[[160, 164, 150],
        [161, 165, 151],
        [161, 165, 151],
        ...,
        [162, 171, 159],
        [162, 171, 159],
        [162, 171, 159]],

       [[159, 163, 149],
        [160, 164, 150],
        [161, 165, 151],
        ...,
        [162, 171, 159],
        [162, 171, 159],
        [161, 170, 158]],

       [[159, 163, 149],
        [159, 163, 149],
        [159, 163, 149],
        ...,
        [160, 169, 157],
        [160, 169, 157],
        [159, 168, 156]],

       ...,

       [[ 62, 109, 157],
        [ 62, 109, 157],
        [ 62, 109, 157],
        ...,
        [ 72, 116, 161],
        [ 77, 121, 166],
        [ 80, 124, 169]],

       [[ 62, 109, 157],
        [ 61, 108, 156],
        [ 61, 108, 156],
        ...,
        [ 62, 106, 151],
        [ 64, 108, 153],
        [ 66, 110, 155]],

       [[ 62, 109, 157],
        [ 61, 108, 156],
        [ 61, 108, 156],
        ...,
        [ 63, 107, 152],
        [ 63, 107, 152],
        [ 64, 108, 153]]], dtype=uint8))
>>> help(video.set)
Help on built-in function set:

set(...) method of cv2.VideoCapture instance
    set(propId, value) -> retval
    .   @brief Sets a property in the VideoCapture.
    .   
    .   @param propId Property identifier from cv::VideoCaptureProperties (eg. cv::CAP_PROP_POS_MSEC, cv::CAP_PROP_POS_FRAMES, ...)
    .   or one from @ref videoio_flags_others
    .   @param value Value of the property.
    .   @return `true` if the property is supported by backend used by the VideoCapture instance.
    .   @note Even if it returns `true` this doesn't ensure that the property
    .   value has been accepted by the capture device. See note in VideoCapture::get()

>>> 
    There is an error (expected an indented block) at line 26, column 1.
>>> 
    There is an error (expected an indented block) at line 32, column 5.
>>> # Run Region [23-35]
Traceback (most recent call last):
  File "<string>", line 23, in <module>
NameError: name 'cv' is not defined
>>> # Run Region [23-35]
Traceback (most recent call last):
  File "<string>", line 23, in <module>
NameError: name 'videoPath' is not defined
>>> # Run Region [6-7]
>>> # Run Region [23-35]
Traceback (most recent call last):
  File "<string>", line 28, in <module>
NameError: name 'cv' is not defined
>>> # Run Region [23-35]
Traceback (most recent call last):
  File "<string>", line 31, in <module>
NameError: name 'cv' is not defined
>>> # Run Region [23-35]
Traceback (most recent call last):
  File "<string>", line 31, in <module>
NameError: name 'cv' is not defined
>>> 
============== RESTART: F:/Users/Administrator/Downloads/cr2.py ==============
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr2.py", line 28, in <module>
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\imgproc\src\color.cpp:181: error: (-215:Assertion failed) !_src.empty() in function 'cv::cvtColor'

>>> # Run Region [23-35]
Traceback (most recent call last):
  File "<string>", line 28, in <module>
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\imgproc\src\color.cpp:181: error: (-215:Assertion failed) !_src.empty() in function 'cv::cvtColor'

>>> # Run Region [line 26]
>>> ret
False
>>> # Run Region [23-35]
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading frames
 error in reading framesTraceback (most recent call last):
  File "<string>", line 35, in <module>
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\PyShell.py", line 1344, in write
    return self.shell.write(s, self.tags)
KeyboardInterrupt
>>> 
=============================== RESTART: Shell ===============================
>>> # Run Region [23-36]
Traceback (most recent call last):
  File "<string>", line 23, in <module>
NameError: name 'cv2' is not defined
>>> 
============== RESTART: F:/Users/Administrator/Downloads/cr2.py ==============
 error in reading frames
>>> 
============== RESTART: F:/Users/Administrator/Downloads/cr2.py ==============
 error in reading frames
>>> 
============== RESTART: F:/Users/Administrator/Downloads/cr2.py ==============
 error in reading frames
>>> # Run Region [23-35]
 error in reading frames
>>> 
============== RESTART: F:/Users/Administrator/Downloads/cr2.py ==============
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr2.py", line 28, in <module>
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
NameError: name 'cv' is not defined
>>> 
============== RESTART: F:/Users/Administrator/Downloads/cr2.py ==============
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr2.py", line 28, in <module>
    gray = cv2.cvtColor(frame, cv.COLOR_BGR2GRAY)
NameError: name 'cv' is not defined
>>> 
============== RESTART: F:/Users/Administrator/Downloads/cr2.py ==============
 error in reading frames
>>> # Run Region [11-21]
Traceback (most recent call last):
  File "<string>", line 15, in <module>
TypeError: imshow() missing required argument 'mat' (pos 2)
>>> # Run Region [11-21]
>>> # Run Region [24-33]
>>> # Run Region [24-33]
Traceback (most recent call last):
  File "<string>", line 31, in <module>
AttributeError: 'builtin_function_or_method' object has no attribute 'sleep'
>>> # Run Region [10-22]
>>> # Run Region [10-22]
>>> # Run Region [25-34]
Traceback (most recent call last):
  File "<string>", line 32, in <module>
AttributeError: 'builtin_function_or_method' object has no attribute 'sleep'
>>> from time.time import sleep
Traceback (most recent call last):
  File "<pyshell#245>", line 1, in <module>
    from time.time import sleep
ModuleNotFoundError: No module named 'time.time'; 'time' is not a package
>>> import time
>>> time.sleep# Run Region [line 3]
>>> # Run Region [25-34]
>>> # Run Region [25-36]
Traceback (most recent call last):
  File "<string>", line 32, in <module>
NameError: name 'cv' is not defined
>>> # Run Region [25-36]
Traceback (most recent call last):
  File "<string>", line 32, in <module>
NameError: name 'cv' is not defined
>>> # Run Region [25-36]
>>> # Run Region [25-36]
>>> # Run Region [25-42]
Traceback (most recent call last):
  File "<string>", line 31, in <module>
NameError: name 'file' is not defined
>>> # Run Region [25-42]
Traceback (most recent call last):
  File "<string>", line 31, in <module>
NameError: name 'file' is not defined
>>> # Run Region [25-42]
Traceback (most recent call last):
  File "<string>", line 31, in <module>
NameError: name 'file' is not defined
>>> # Run Region [25-42]
Traceback (most recent call last):
  File "<string>", line 35, in <module>
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

>>> 
============== RESTART: F:/Users/Administrator/Downloads/cr3.py ==============
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr3.py", line 17, in <module>
    rgb(0)
  File "F:/Users/Administrator/Downloads/cr3.py", line 9, in rgb
    img[:] = [b, g, r]
UnboundLocalError: local variable 'img' referenced before assignment
>>> 
============== RESTART: F:/Users/Administrator/Downloads/cr3.py ==============
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr3.py", line 25, in <module>
    rgb(0)
  File "F:/Users/Administrator/Downloads/cr3.py", line 17, in rgb
    img[:] = [b, g, r]
UnboundLocalError: local variable 'img' referenced before assignment
>>> 
============== RESTART: F:/Users/Administrator/Downloads/cr3.py ==============
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr3.py", line 20, in <module>
    rgb(0)
  File "F:/Users/Administrator/Downloads/cr3.py", line 13, in rgb
    cv.displayOverlay('window', f'Red={r}, Green={g}, Blue={b}')
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

>>> 
============== RESTART: F:/Users/Administrator/Downloads/cr3.py ==============
>>> 
============== RESTART: F:/Users/Administrator/Downloads/cr3.py ==============
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr3.py", line 21, in <module>
    rgb(0)
  File "F:/Users/Administrator/Downloads/cr3.py", line 15, in rgb
    time.sleep(1)
NameError: name 'time' is not defined
>>> 
============== RESTART: F:/Users/Administrator/Downloads/cr3.py ==============
>>> 
============== RESTART: F:/Users/Administrator/Downloads/cr3.py ==============
>>> import pyqt
Traceback (most recent call last):
  File "<pyshell#247>", line 1, in <module>
    import pyqt
ModuleNotFoundError: No module named 'pyqt'
>>> img= np.zeros((100,600,3))
>>> r
Traceback (most recent call last):
  File "<pyshell#249>", line 1, in <module>
    r
NameError: name 'r' is not defined
>>> r= cv.getTrackbarPos('red','window')
>>> img[:] = [r, r, r]
>>> cv.imshow('window',img)
>>> # Run Region [8-12]
>>> # Run Region [line 14]
>>> # Run Region [line 16]
>>> # Run Region [line 17]
>>> # Run Region [line 18]
>>> # Run Region [line 19]
>>> # Run Region [line 20]
>>> # Run Region [12-17]
>>> # Run Region [2-10]
>>> # Run Region [12-14]
>>> Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 7, in mouse
cv2.error: OpenCV(4.0.1) C:\ci\opencv-suite_1573470242804\work\modules\highgui\src\window.cpp:548: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayOverlay'

# Run Region [5-14]
>>> help(cv.imread)
Help on built-in function imread:

imread(...)
    imread(filename[, flags]) -> retval
    .   @brief Loads an image from a file.
    .   
    .   @anchor imread
    .   
    .   The function imread loads an image from the specified file and returns it. If the image cannot be
    .   read (because of missing file, improper permissions, unsupported or invalid format), the function
    .   returns an empty matrix ( Mat::data==NULL ).
    .   
    .   Currently, the following file formats are supported:
    .   
    .   -   Windows bitmaps - \*.bmp, \*.dib (always supported)
    .   -   JPEG files - \*.jpeg, \*.jpg, \*.jpe (see the *Note* section)
    .   -   JPEG 2000 files - \*.jp2 (see the *Note* section)
    .   -   Portable Network Graphics - \*.png (see the *Note* section)
    .   -   WebP - \*.webp (see the *Note* section)
    .   -   Portable image format - \*.pbm, \*.pgm, \*.ppm \*.pxm, \*.pnm (always supported)
    .   -   PFM files - \*.pfm (see the *Note* section)
    .   -   Sun rasters - \*.sr, \*.ras (always supported)
    .   -   TIFF files - \*.tiff, \*.tif (see the *Note* section)
    .   -   OpenEXR Image files - \*.exr (see the *Note* section)
    .   -   Radiance HDR - \*.hdr, \*.pic (always supported)
    .   -   Raster and Vector geospatial data supported by GDAL (see the *Note* section)
    .   
    .   @note
    .   -   The function determines the type of an image by the content, not by the file extension.
    .   -   In the case of color images, the decoded images will have the channels stored in **B G R** order.
    .   -   When using IMREAD_GRAYSCALE, the codec's internal grayscale conversion will be used, if available.
    .   Results may differ to the output of cvtColor()
    .   -   On Microsoft Windows\* OS and MacOSX\*, the codecs shipped with an OpenCV image (libjpeg,
    .   libpng, libtiff, and libjasper) are used by default. So, OpenCV can always read JPEGs, PNGs,
    .   and TIFFs. On MacOSX, there is also an option to use native MacOSX image readers. But beware
    .   that currently these native image loaders give images with different pixel values because of
    .   the color management embedded into MacOSX.
    .   -   On Linux\*, BSD flavors and other Unix-like open-source operating systems, OpenCV looks for
    .   codecs supplied with an OS image. Install the relevant packages (do not forget the development
    .   files, for example, "libjpeg-dev", in Debian\* and Ubuntu\*) to get the codec support or turn
    .   on the OPENCV_BUILD_3RDPARTY_LIBS flag in CMake.
    .   -   In the case you set *WITH_GDAL* flag to true in CMake and @ref IMREAD_LOAD_GDAL to load the image,
    .   then the [GDAL](http://www.gdal.org) driver will be used in order to decode the image, supporting
    .   the following formats: [Raster](http://www.gdal.org/formats_list.html),
    .   [Vector](http://www.gdal.org/ogr_formats.html).
    .   -   If EXIF information are embedded in the image file, the EXIF orientation will be taken into account
    .   and thus the image will be rotated accordingly except if the flag @ref IMREAD_IGNORE_ORIENTATION is passed.
    .   -   Use the IMREAD_UNCHANGED flag to keep the floating point values from PFM image.
    .   -   By default number of pixels must be less than 2^30. Limit can be set using system
    .   variable OPENCV_IO_MAX_IMAGE_PIXELS
    .   
    .   @param filename Name of file to be loaded.
    .   @param flags Flag that can take values of cv::ImreadModes

>>> help(cv.imshow)
Help on built-in function imshow:

imshow(...)
    imshow(winname, mat) -> None
    .   @brief Displays an image in the specified window.
    .   
    .   The function imshow displays an image in the specified window. If the window was created with the
    .   cv::WINDOW_AUTOSIZE flag, the image is shown with its original size, however it is still limited by the screen resolution.
    .   Otherwise, the image is scaled to fit the window. The function may scale the image, depending on its depth:
    .   
    .   -   If the image is 8-bit unsigned, it is displayed as is.
    .   -   If the image is 16-bit unsigned or 32-bit integer, the pixels are divided by 256. That is, the
    .   value range [0,255\*256] is mapped to [0,255].
    .   -   If the image is 32-bit or 64-bit floating-point, the pixel values are multiplied by 255. That is, the
    .   value range [0,1] is mapped to [0,255].
    .   
    .   If window was created with OpenGL support, cv::imshow also support ogl::Buffer , ogl::Texture2D and
    .   cuda::GpuMat as input.
    .   
    .   If the window was not created before this function, it is assumed creating a window with cv::WINDOW_AUTOSIZE.
    .   
    .   If you need to show an image that is bigger than the screen resolution, you will need to call namedWindow("", WINDOW_NORMAL) before the imshow.
    .   
    .   @note This function should be followed by cv::waitKey function which displays the image for specified
    .   milliseconds. Otherwise, it won't display the image. For example, **waitKey(0)** will display the window
    .   infinitely until any keypress (it is suitable for image display). **waitKey(25)** will display a frame
    .   for 25 ms, after which display will be automatically closed. (If you put it in a loop to read
    .   videos, it will display the video frame-by-frame)
    .   
    .   @note
    .   
    .   [__Windows Backend Only__] Pressing Ctrl+C will copy the image to the clipboard.
    .   
    .   [__Windows Backend Only__] Pressing Ctrl+S will show a dialog to save the image.
    .   
    .   @param winname Name of the window.
    .   @param mat Image to be shown.

>>> # Run Region [12-14]
>>> # Run Region [14-16]
>>> # Run Region [14-16]
>>> scale=10
>>> rows,cols= img.shape[:2]
>>> img2= cv.resize(img,(scale*cols, scale*rows),interpolation=cv.INTER_LINEAR)
>>> cv.imshow('window',img2)
>>> cv.imshow('window',img2)
>>> img[1,100]
array([255, 255, 255], dtype=uint8)
>>> 
============== RESTART: F:/Users/Administrator/Downloads/cr3.py ==============
>>> 
============== RESTART: F:/Users/Administrator/Downloads/cr3.py ==============
>>> Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr3.py", line 7, in mouse
    img[y/2, x/2] = [0, 0, 255]
IndexError: only integers, slices (`:`), ellipsis (`...`), numpy.newaxis (`None`) and integer or boolean arrays are valid indices
Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr3.py", line 7, in mouse
    img[y/2, x/2] = [0, 0, 255]
IndexError: only integers, slices (`:`), ellipsis (`...`), numpy.newaxis (`None`) and integer or boolean arrays are valid indices
Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr3.py", line 7, in mouse
    img[y/2, x/2] = [0, 0, 255]
IndexError: only integers, slices (`:`), ellipsis (`...`), numpy.newaxis (`None`) and integer or boolean arrays are valid indices
Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr3.py", line 7, in mouse
    img[y/2, x/2] = [0, 0, 255]
IndexError: only integers, slices (`:`), ellipsis (`...`), numpy.newaxis (`None`) and integer or boolean arrays are valid indices
Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr3.py", line 7, in mouse
    img[y/2, x/2] = [0, 0, 255]
IndexError: only integers, slices (`:`), ellipsis (`...`), numpy.newaxis (`None`) and integer or boolean arrays are valid indices
Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr3.py", line 7, in mouse
    img[y/2, x/2] = [0, 0, 255]
IndexError: only integers, slices (`:`), ellipsis (`...`), numpy.newaxis (`None`) and integer or boolean arrays are valid indices
Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr3.py", line 7, in mouse
    img[y/2, x/2] = [0, 0, 255]
IndexError: only integers, slices (`:`), ellipsis (`...`), numpy.newaxis (`None`) and integer or boolean arrays are valid indices
Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr3.py", line 7, in mouse
    img[y/2, x/2] = [0, 0, 255]
IndexError: only integers, slices (`:`), ellipsis (`...`), numpy.newaxis (`None`) and integer or boolean arrays are valid indices
Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr3.py", line 7, in mouse
    img[y/2, x/2] = [0, 0, 255]
IndexError: only integers, slices (`:`), ellipsis (`...`), numpy.newaxis (`None`) and integer or boolean arrays are valid indices
Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr3.py", line 7, in mouse
    img[y/2, x/2] = [0, 0, 255]
IndexError: only integers, slices (`:`), ellipsis (`...`), numpy.newaxis (`None`) and integer or boolean arrays are valid indices
Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr3.py", line 7, in mouse
    img[y/2, x/2] = [0, 0, 255]
IndexError: only integers, slices (`:`), ellipsis (`...`), numpy.newaxis (`None`) and integer or boolean arrays are valid indices
Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr3.py", line 7, in mouse
    img[y/2, x/2] = [0, 0, 255]
IndexError: only integers, slices (`:`), ellipsis (`...`), numpy.newaxis (`None`) and integer or boolean arrays are valid indices
Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr3.py", line 7, in mouse
    img[y/2, x/2] = [0, 0, 255]
IndexError: only integers, slices (`:`), ellipsis (`...`), numpy.newaxis (`None`) and integer or boolean arrays are valid indices
Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr3.py", line 7, in mouse
    img[y/2, x/2] = [0, 0, 255]
IndexError: only integers, slices (`:`), ellipsis (`...`), numpy.newaxis (`None`) and integer or boolean arrays are valid indices
Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr3.py", line 7, in mouse
    img[y/2, x/2] = [0, 0, 255]
IndexError: only integers, slices (`:`), ellipsis (`...`), numpy.newaxis (`None`) and integer or boolean arrays are valid indices
Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr3.py", line 7, in mouse
    img[y/2, x/2] = [0, 0, 255]
IndexError: only integers, slices (`:`), ellipsis (`...`), numpy.newaxis (`None`) and integer or boolean arrays are valid indices
Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr3.py", line 7, in mouse
    img[y/2, x/2] = [0, 0, 255]
IndexError: only integers, slices (`:`), ellipsis (`...`), numpy.newaxis (`None`) and integer or boolean arrays are valid indices
Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr3.py", line 7, in mouse
    img[y/2, x/2] = [0, 0, 255]
IndexError: only integers, slices (`:`), ellipsis (`...`), numpy.newaxis (`None`) and integer or boolean arrays are valid indices
Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr3.py", line 7, in mouse
    img[y/2, x/2] = [0, 0, 255]
IndexError: only integers, slices (`:`), ellipsis (`...`), numpy.newaxis (`None`) and integer or boolean arrays are valid indices
Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr3.py", line 7, in mouse
    img[y/2, x/2] = [0, 0, 255]
IndexError: only integers, slices (`:`), ellipsis (`...`), numpy.newaxis (`None`) and integer or boolean arrays are valid indices
Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr3.py", line 7, in mouse
    img[y/2, x/2] = [0, 0, 255]
IndexError: only integers, slices (`:`), ellipsis (`...`), numpy.newaxis (`None`) and integer or boolean arrays are valid indices
Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr3.py", line 7, in mouse
    img[y/2, x/2] = [0, 0, 255]
IndexError: only integers, slices (`:`), ellipsis (`...`), numpy.newaxis (`None`) and integer or boolean arrays are valid indices
Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr3.py", line 7, in mouse
    img[y/2, x/2] = [0, 0, 255]
IndexError: only integers, slices (`:`), ellipsis (`...`), numpy.newaxis (`None`) and integer or boolean arrays are valid indices
Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr3.py", line 7, in mouse
    img[y/2, x/2] = [0, 0, 255]
IndexError: only integers, slices (`:`), ellipsis (`...`), numpy.newaxis (`None`) and integer or boolean arrays are valid indices
Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr3.py", line 7, in mouse
    img[y/2, x/2] = [0, 0, 255]
IndexError: only integers, slices (`:`), ellipsis (`...`), numpy.newaxis (`None`) and integer or boolean arrays are valid indices
Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr3.py", line 7, in mouse
    img[y/2, x/2] = [0, 0, 255]
IndexError: only integers, slices (`:`), ellipsis (`...`), numpy.newaxis (`None`) and integer or boolean arrays are valid indices
Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr3.py", line 7, in mouse
    img[y/2, x/2] = [0, 0, 255]
IndexError: only integers, slices (`:`), ellipsis (`...`), numpy.newaxis (`None`) and integer or boolean arrays are valid indices
Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr3.py", line 7, in mouse
    img[y/2, x/2] = [0, 0, 255]
IndexError: only integers, slices (`:`), ellipsis (`...`), numpy.newaxis (`None`) and integer or boolean arrays are valid indices
Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr3.py", line 7, in mouse
    img[y/2, x/2] = [0, 0, 255]
IndexError: only integers, slices (`:`), ellipsis (`...`), numpy.newaxis (`None`) and integer or boolean arrays are valid indices
Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr3.py", line 7, in mouse
    img[y/2, x/2] = [0, 0, 255]
IndexError: only integers, slices (`:`), ellipsis (`...`), numpy.newaxis (`None`) and integer or boolean arrays are valid indices
Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr3.py", line 7, in mouse
    img[y/2, x/2] = [0, 0, 255]
IndexError: only integers, slices (`:`), ellipsis (`...`), numpy.newaxis (`None`) and integer or boolean arrays are valid indices
Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr3.py", line 7, in mouse
    img[y/2, x/2] = [0, 0, 255]
IndexError: only integers, slices (`:`), ellipsis (`...`), numpy.newaxis (`None`) and integer or boolean arrays are valid indices
Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr3.py", line 7, in mouse
    img[y/2, x/2] = [0, 0, 255]
IndexError: only integers, slices (`:`), ellipsis (`...`), numpy.newaxis (`None`) and integer or boolean arrays are valid indices
Traceback (most recent call last):
  File "F:\Users\Administrator\Downloads\idlex-1.18\idlexlib\idlefork\idlelib\run.py", line 119, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "F:\Anaconda3\envs\deepxde\lib\queue.py", line 178, in get
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr3.py", line 7, in mouse
    img[y/2, x/2] = [0, 0, 255]
IndexError: only integers, slices (`:`), ellipsis (`...`), numpy.newaxis (`None`) and integer or boolean arrays are valid indices
KeyboardInterrupt
>>> 10\2
SyntaxError: unexpected character after line continuation character
>>> round(10/2)
5
>>> round(10/3)
3
>>> 
============== RESTART: F:/Users/Administrator/Downloads/cr3.py ==============
>>> 
============== RESTART: F:/Users/Administrator/Downloads/cr3.py ==============
>>> import cv2 as cv
>>> events = [i for i in dir(cv) if 'EVENT' in i]
>>> print( events )
['EVENT_FLAG_ALTKEY', 'EVENT_FLAG_CTRLKEY', 'EVENT_FLAG_LBUTTON', 'EVENT_FLAG_MBUTTON', 'EVENT_FLAG_RBUTTON', 'EVENT_FLAG_SHIFTKEY', 'EVENT_LBUTTONDBLCLK', 'EVENT_LBUTTONDOWN', 'EVENT_LBUTTONUP', 'EVENT_MBUTTONDBLCLK', 'EVENT_MBUTTONDOWN', 'EVENT_MBUTTONUP', 'EVENT_MOUSEHWHEEL', 'EVENT_MOUSEMOVE', 'EVENT_MOUSEWHEEL', 'EVENT_RBUTTONDBLCLK', 'EVENT_RBUTTONDOWN', 'EVENT_RBUTTONUP']
>>> 
============== RESTART: F:/Users/Administrator/Downloads/cr4.py ==============
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 30, in <module>
    if cv2.waitKey(1) & 0xFF == 27:
KeyboardInterrupt
>>> 
KeyboardInterrupt
>>> 
============== RESTART: F:/Users/Administrator/Downloads/cr3.py ==============
>>> 
============== RESTART: F:/Users/Administrator/Downloads/cr4.py ==============
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 31, in <module>
    if cv2.waitKey(1) & 0xFF == 27:
KeyboardInterrupt
>>> img2=cv2.resize(img,(512,512,3))
Traceback (most recent call last):
  File "<pyshell#268>", line 1, in <module>
    img2=cv2.resize(img,(512,512,3))
TypeError: function takes exactly 2 arguments (3 given)
>>> 
============== RESTART: F:/Users/Administrator/Downloads/cr4.py ==============
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 33, in <module>
    if cv2.waitKey(1) & 0xFF == 27:
KeyboardInterrupt
>>> img
array([[[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
        ...,
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]],

       [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
        ...,
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]],

       [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
        ...,
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]],

       ...,

       [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
        ...,
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]],

       [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
        ...,
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]],

       [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
        ...,
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]], dtype=uint8)
>>> img[:]=225
>>> img
array([[[225, 225, 225],
        [225, 225, 225],
        [225, 225, 225],
        ...,
        [225, 225, 225],
        [225, 225, 225],
        [225, 225, 225]],

       [[225, 225, 225],
        [225, 225, 225],
        [225, 225, 225],
        ...,
        [225, 225, 225],
        [225, 225, 225],
        [225, 225, 225]],

       [[225, 225, 225],
        [225, 225, 225],
        [225, 225, 225],
        ...,
        [225, 225, 225],
        [225, 225, 225],
        [225, 225, 225]],

       ...,

       [[225, 225, 225],
        [225, 225, 225],
        [225, 225, 225],
        ...,
        [225, 225, 225],
        [225, 225, 225],
        [225, 225, 225]],

       [[225, 225, 225],
        [225, 225, 225],
        [225, 225, 225],
        ...,
        [225, 225, 225],
        [225, 225, 225],
        [225, 225, 225]],

       [[225, 225, 225],
        [225, 225, 225],
        [225, 225, 225],
        ...,
        [225, 225, 225],
        [225, 225, 225],
        [225, 225, 225]]], dtype=uint8)
>>> # Run Region [30-36]
Traceback (most recent call last):
  File "<string>", line 35, in <module>
KeyboardInterrupt
>>> # Run Region [33-37]
Traceback (most recent call last):
  File "<string>", line 35, in <module>
KeyboardInterrupt
>>> # Run Region [30-37]
>>> 
============== RESTART: F:/Users/Administrator/Downloads/cr4.py ==============
>>> 
============== RESTART: F:/Users/Administrator/Downloads/cr4.py ==============
>>> 
============== RESTART: F:/Users/Administrator/Downloads/cr4.py ==============
>>> import cv2
>>> 
============== RESTART: F:/Users/Administrator/Downloads/cr4.py ==============
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 26, in line_drawing
    cv2.imshow()
TypeError: imshow() missing required argument 'winname' (pos 1)
>>> 
============== RESTART: F:/Users/Administrator/Downloads/cr4.py ==============
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 26, in line_drawing
    cv2.imshow('')
TypeError: imshow() missing required argument 'mat' (pos 2)
>>> 
============== RESTART: F:/Users/Administrator/Downloads/cr4.py ==============
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 24, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 24, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
>>> 
============== RESTART: F:/Users/Administrator/Downloads/cr4.py ==============
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 20, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
Traceback (most recent call last):
  File "F:/Users/Administrator/Downloads/cr4.py", line 24, in line_drawing
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
UnboundLocalError: local variable 'img' referenced before assignment
>>> 
============== RESTART: F:/Users/Administrator/Downloads/cr4.py ==============

============== RESTART: F:/Users/Administrator/Downloads/cr4.py ==============

============== RESTART: F:/Users/Administrator/Downloads/cr2.py ==============
>>> 
