# ROI Predictor for AI Projects

This is a Streamlit web application that predicts the Return on Investment (ROI) for artificial intelligence projects. It allows you to specify project parameters such as investment amount, project duration, technical complexity and potential impact, and uses a trained Random Forest model to estimate the expected ROI. The interface embraces a modern look with purple tones and the ability to display an Accenture logo if provided. After making a prediction, the app also explains which factors had the greatest influence on the estimate by showing feature importances in a bar chart and listing them in order of significance.

## Features
- Interactive sliders in a sidebar to adjust the input parameters of an AI project
- Real-time ROI prediction using a Random Forest regressor trained on sample data
- Visualization of feature importance so you can understand which inputs drive the prediction
- Customizable theme: purple styling for a professional look and optional inclusion of an Accenture logo
- Lightweight CSV dataset (`progetti_ai.csv`) used to train the model, easy to extend or replace with your own data

## Setup Instructions

To run the app locally on your computer, follow these steps:

1. Make sure you have Python installed (preferably Python 3.7 or later). If you don't already have it, download it from the [official Python website](https://www.python.org/downloads/).
2. Clone or download this repository to your local machine.
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```
3. (Optional) Create and activate a virtual environment to isolate dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate    # On Linux/Mac
   venv\Scripts ctivate     # On Windows
   ```
4. Install the required Python packages using the provided `requirements.txt` file:
   ```bash
   pip install -r requirements.txt
   ```
5. Run the Streamlit app:
   ```bash
   streamlit run streamlit_app.py
   ```
6. Your default web browser should automatically open and display the application at `http://localhost:8501`. If it doesn't, navigate to that address manually.

## Usage

Once the app is running, interact with it as follows:

- Use the sliders in the left sidebar to set values for **Investments (millions EUR)**, **Duration (months)**, **Technical Complexity**, and **Potential Impact**. The sliders are automatically scaled based on the sample data.
- After adjusting the inputs, the ROI prediction appears under the "Predizione del ROI" header. The number represents the expected ROI in millions of EUR.
- Scroll down to the "Fattori Che Influenzano la Predizione" (Factors Influencing the Prediction) section to see a bar chart of feature importances. Below the chart, a textual list shows the same importance values ranked from highest to lowest. This helps you understand which inputs had the greatest effect on your prediction.
- If you want to change the logo displayed at the top of the page, replace the file `accenture_logo.png` in the project root with your own image. Streamlit will automatically detect the file and display it. If the file is absent or incorrectly named, the placeholder simply disappears without breaking the app.

## Deployment on Streamlit Cloud

To publish your app online via the free Streamlit Community Cloud service, follow these steps:

1. Push your project to a GitHub repository. Make sure it contains at least these files: `streamlit_app.py`, `progetti_ai.csv`, `requirements.txt`, and optionally your `accenture_logo.png`.
2. Go to [Streamlit Community Cloud](https://share.streamlit.io/) and sign in with your GitHub account. If you haven't connected your GitHub account yet, click "Connect GitHub" from the top bar and authorize Streamlit to access your repositories.
3. Click on the button **New app** or **Create app** in the Streamlit Cloud dashboard.
4. Select the repository you pushed in step 1, choose the branch (usually `main` or `master`) and specify the main file path as `streamlit_app.py`. Press **Deploy**.
5. Wait a few moments while Streamlit Cloud installs your dependencies and spins up a server. Once completed, you will be given a public URL where your live app can be accessed from any device.
6. If you need to update the app, commit changes to your GitHub repository. Streamlit Cloud monitors the repo and will offer you to redeploy or automatically redeploy on every push, depending on your settings.

### Troubleshooting Tips
- Ensure your `requirements.txt` lists all the necessary packages (`streamlit`, `pandas`, `numpy`, `scikit-learn` at a minimum). Without it, the deploy will fail because dependencies cannot be installed on the remote server.
- Make sure the main file name matches exactly the string you input during creation (`streamlit_app.py`). Typos in names prevent the app from launching.
- If the deploy process fails or the app shows errors, click on the **Logs** tab in your Streamlit Cloud dashboard for detailed messages about missing packages or other issues.

## Customization

You can easily customize or extend this project:

- Modify the underlying model or replace the training data: load your own CSV in the `load_data` function and re-train or re-fit the model.
- Adjust the range or type of input widgets in the sidebar (e.g. use `st.number_input`, `st.selectbox`, etc.) to reflect real parameter ranges or categorical choices.
- Tweak the CSS in the `st.markdown` call at the top of `streamlit_app.py` to adjust colors, spacing and fonts to your brand guidelines or personal taste.
- Add additional explanatory text, images or documentation anywhere in the app by using `st.markdown`, `st.image`, `st.write`, etc.

## License and Acknowledgements

This project is provided for educational purposes. Feel free to adapt the code for your own analytics or business contexts. The data in `progetti_ai.csv` is synthetic sample data; replace it with real input data for realistic modeling. The logo shown in the interface belongs to Accenture as part of styling demonstration; you must have rights to display any trademarked images you include.
