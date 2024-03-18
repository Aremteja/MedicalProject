from keras.models import load_model


class MLModel:
    def __init__(self, model_path):
        self.model = load_model(model_path)

    def predict(self, input_data):
        #Perform prediction using the loaded model
        prediction = self.model.predict(input_data)
        return prediction
    