import cv2
import numpy as np


def evaluate(filepath, model):
    test_x = []
    image = cv2.imread(filepath)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = cv2.resize(image, (299, 299), interpolation=cv2.INTER_AREA)
    test_x.append(image)

    # Then pre-process the test image:
    test_x = np.asarray(test_x)
    test_processed_x = test_x.astype("float") / 255.0
    # Then you can predict from your model like this:

    test_predictions = model.predict(test_processed_x, batch_size=1)

    print(test_predictions)
    res = max(*test_predictions.tolist())
    problem = test_predictions.tolist()[0].index(res)
    if problem == 0:
        result = 'all right!'
    elif problem == 1:
        result = 'horizon crooked to the left'
    elif problem == 2:
        result = 'not realistic enough'
    elif problem == 3:
        result = 'horizon crooked to the right'
    elif problem == 4:
        result = 'too dark'
    elif problem == 5:
        result = 'too bright'
    return result


