# Art Movement Detector

This project aims to detect the art style of an image using the ViT (Vision Transformer) model. It includes a Flask API for making predictions and a frontend built with HTML and CSS.

## Installation

1. Clone the repository:
   git clone https://github.com/Jagannath/artDetection.git
   
   cd artDetection

3. Install the required Python packages:
   pip install -r requirements.txt

4. Download the pre-trained model checkpoint:
   The pre-trained model checkpoint should be downloaded and saved in the "vit-base-beans/checkpoint-200" directory. You can obtain the checkpoint from Hugging Face Model Hub at https://huggingface.co/google/vit-base-patch16-224.

## Usage

1. Start the Flask API:
   python main.py
   The API will be available at http://localhost:5000.

2. Open the frontend:
   Open the "index.html" file in your web browser. You can interact with the web interface to upload an image and get the predicted art style.

## Project Structure

- main.py: Flask application script that serves the API endpoints.
- index.html: HTML file for the frontend user interface.
- style.css: CSS file for styling the frontend.
- vit-base-beans/checkpoint-200: Directory containing the pre-trained model checkpoint.
- README.md: Project documentation.

## Additional Notes

- This project uses the ViT (Vision Transformer) model for image classification. The model is fine-tuned on the art style recognition task using the "Jagannath/artRecognition" dataset.
- The Flask API exposes a single endpoint "/predict" that accepts an image file and returns the predicted art style as a JSON response.
- - The model is implemented using PyTorch and trained using pytorch.
- The frontend provides a user-friendly interface for uploading an image and displaying the predicted art style.
- You can test out the mdoel directly at https://huggingface.co/Jagannath/artDetection

Feel free to customize the project structure and files according to your requirements.

## Acknowledgments

- The ViT model and training code are based on the Hugging Face Transformers library.
- The art style recognition dataset ("Jagannath/artRecognition") is used for fine-tuning the model.
