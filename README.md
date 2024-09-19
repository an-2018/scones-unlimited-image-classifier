
# Scones Unlimited - Image Classification Model

## Project Overview

This project is part of the Udacity AWS Machine Learning Fundamentals where we learn different topics within Machine Learning and implement then in different projects. In this scenario we have Scones Unlimited a logistics company focused on scone deliveries. This project involves building an image classification model that can differentiate between bicycles and motorcycles to help optimize delivery operations. The image classification model will route delivery professionals based on their vehicle type, improving operational efficiency.

The project is built using AWS SageMaker for model development, AWS Lambda for building supporting services, and AWS Step Functions for creating an event-driven application. The model will be scalable and monitored for performance to ensure reliability in a production environment.

## Table of Contents

- [Scones Unlimited - Image Classification Model](#scones-unlimited---image-classification-model)
  - [Project Overview](#project-overview)
  - [Table of Contents](#table-of-contents)
  - [Project Motivation](#project-motivation)
  - [Project Structure](#project-structure)
  - [Project Steps](#project-steps)
  - [Technologies Used](#technologies-used)
  - [Getting Started](#getting-started)
  - [Testing](#testing)
  - [Future Enhancements](#future-enhancements)

## Project Motivation

Image classifiers are widely used in industries like autonomous vehicles, augmented reality, eCommerce, and diagnostic medicine. This project demonstrates how machine learning can improve delivery operations by routing drivers based on their vehicle type, enabling Scones Unlimited to efficiently handle bicycle and motorcycle deliveries.

## Project Structure

The project is structured into several key steps, which are outlined below:

```
.
├── data                # Data staging files and dataset details
├── model               # SageMaker model training and deployment code
├── lambdas             # AWS Lambda functions for model interaction
├── step_functions      # AWS Step Functions workflow definitions
├── tests               # Scripts to test the deployed model and services
└── README.md           # Project documentation (this file)
```

## Project Steps

1. **Data Staging**: 
   - Gather and preprocess images of bicycles and motorcycles for training.
   - Store data in S3 for easy access by SageMaker.

2. **Model Training and Deployment**:
   - Use AWS SageMaker to train an image classification model to distinguish between bicycles and motorcycles.
   - Deploy the model to an endpoint for inference.

3. **Lambda Functions and Step Function Workflow**:
   - Create AWS Lambda functions that interact with the model and process incoming requests.
   - Use AWS Step Functions to orchestrate the workflow that includes invoking Lambdas and performing model inference.

4. **Testing and Evaluation**:
   - Evaluate model performance using a test dataset.
   - Test the entire pipeline, including Lambda functions and Step Functions, to ensure correct behavior in a production environment.

5. **Optional Challenge**:
   - Enhance the project by adding monitoring to detect model drift or optimize model performance.

6. **Cleanup Cloud Resources**:
   - Remove or disable AWS resources to avoid unnecessary charges after completing the project.

## Technologies Used

- **AWS SageMaker**: For model training, deployment, and inference.
- **AWS Lambda**: For handling inference requests.
- **AWS Step Functions**: For building an event-driven workflow.
- **AWS S3**: For data storage.
- **Python**: For coding the model, Lambda functions, and testing scripts.

## Getting Started

To get started with this project, follow the instructions below:

1. **Clone the repository**:

   ```bash
   git clone <link to repository>
   cd scones-unlimited-image-classifier
   ```

2. **Set up AWS**:

   Ensure you have an AWS account and the AWS CLI set up with appropriate permissions to create and manage SageMaker, Lambda, and Step Functions resources.

3. **Run the Project**:

   - Follow the instructions in each step's directory (`data`, `model`, `lambdas`, `step_functions`) to prepare data, train the model, deploy services, and test the entire workflow.

## Testing

- **Model Testing**: Test the deployed SageMaker model using sample images to ensure it correctly classifies bicycles and motorcycles.
- **End-to-End Testing**: Test the full pipeline by invoking the Step Function workflow and verifying that the Lambda functions interact with the model as expected.

## Future Enhancements

- **Model Monitoring**: Implement AWS CloudWatch metrics and alarms to monitor the model's performance and detect drift.
- **Additional Classification Tasks**: Expand the model to classify more vehicle types (e.g., cars, trucks).
- **Performance Optimization**: Experiment with different model architectures and hyperparameters to improve classification accuracy.
