# dsan5800-final-project
Final Project for DSAN 5800: Advanced Natural Language Processing

Group members:
* Austin Barish
* Marion Bauman
* Hongxin Wu

Potential Models:
| Model | Link | About |
|-------|------|-------|
| xlm-mlm-en-2048 | https://huggingface.co/xlm-mlm-en-2048 | Masked inference model |
| bert-base-cased | [https://huggingface.co/bert-base-cased](https://huggingface.co/bert-base-cased) | Masked inference model, 110M params, High performance |
| roberta-base | https://huggingface.co/roberta-base | Masked inference model, 125M params |
| albert-base-v2 | https://huggingface.co/albert-base-v2 | Masked inference model, 11.8M params |

Potential UIs:
| Name | Link |
|------|------|
| Shiny for Python | [https://shiny.posit.co/py/](https://shiny.posit.co/py/) |
| JavaScript/React | [https://mui.com/material-ui/react-autocomplete/](https://mui.com/material-ui/react-autocomplete/) |
| Flask | https://flask.palletsprojects.com/en/3.0.x/ |

Web Deployment Tools:
| Name | Link |
|------|------|
| Heroku | https://www.heroku.com/ |

## Abstract
This project focuses on addressing the challenge of homophones in written text - words that sound alike but have different meanings or spellings, like 'to', 'too', and 'two'. Recognizing that many standard grammar and spelling checks, including those in smartphones, often overlook these errors, we developed a specialized model to identify and correct such mistakes, ensuring grammatically accurate output.

Our approach involved compiling a comprehensive list of 442 sets of homophones (totaling 941 words), focusing on common homophones in American and English dialects. We then created a test dataset using text from 10 popular books from Project Gutenberg, resulting in 68,573 sentences. To test our model, we artificially inserted homophone errors into these sentences, considering the frequency of each homophone in the dataset to ensure a balanced distribution of errors.

In addition to the homophone correction model, we developed an interactive web application, making our solution accessible and user-friendly. Our web app allows users to input text and receive real-time corrections, with the option to see both homophone and spelling corrections. The app's intuitive design, responsive features, and dual-output correction system demonstrate the practical application of our advanced NLP model in everyday scenarios.

The backend of the web app is powered by Python scripts using Flask for web requests handling and homophone utility files for correction logic. We also ensure the web app is visually appealing and functional across various devices.
