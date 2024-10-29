## Title of the Project
INTELLIGENT REAL-TIME DISASTER RESPONSE DASHBOARD LEVERAGING AI AND SOCIAL MEDIA ANALYTICS

## About
<!--Detailed Description about the project-->
This project aims to create an Intelligent Real-Time Disaster Response Dashboard using AI and social media analytics. By gathering and processing social media posts, the system provides actionable insights to emergency responders, such as identifying the location, type, and severity of incidents, to enhance response efficiency during disaste

## Features
<!--List the features of the project as shown below-->
**Data Extraction and Preprocessing:**
1) Used Python’s pytesseract library to extract text from social media images.
2) Parsed and structured extracted text data into JSON format, with fields like location, issue, description, severity, and affected people.
   
**Data Storage and Management:**
1) Stored structured data in MongoDB for efficient retrieval and analysis.
2) Ensured data integrity and easy access for visualization and further analysis.
   
**Data Analysis:**
1) Analyzed data completeness and consistency to ensure reliability for decision-making.
2) Created charts to represent data quality, such as completeness and unique counts per field.
   
**Dashboard Creation and Visualization:**
1) Used Power BI to develop an interactive dashboard displaying key insights, including:
   1) **Map visualization** for affected locations.
   2) **Bar charts** for incident types and affected populations.
   3) **Donut chart** showing the distribution of incidents by severity.
   4) **Card visual** indicating the total number of affected individuals.
2) Integrated data from MongoDB into Power BI using Python to ensure real-time updates.
- A framework based application for deployment purpose.
- High scalability.
- Less time complexity.
- A specific scope of Chatbot response model, using json data format.

## System Architecture
<!--Embed the system architecture diagram as shown below-->

![image](https://github.com/user-attachments/assets/e17266ac-f77d-488d-b925-76597a49280a)

## Output

<!--Embed the Output picture at respective places as shown below as shown below-->
#### Output1 - Successfully texts are retrieved from posts and loaded into the MongoDB
![image](https://github.com/user-attachments/assets/3ba4fd5a-e676-4417-bfc6-d049c7aa7998)
![image](https://github.com/user-attachments/assets/e2806dbf-6144-4145-aa87-51d77bec4f05)

#### Output2 - Completed Dashboard
![image](https://github.com/user-attachments/assets/4d757653-7205-48a6-a467-c3ccfa12e5a5)

**Data Completion (consumed 100 % of data from posts)**
![image](https://github.com/user-attachments/assets/d60acb0e-8f5a-4588-a603-913cddefed98)

**Chart Consistency by unique values**
![image](https://github.com/user-attachments/assets/9f43a2b6-fa40-4549-b326-6a57fb615c2d)

## Results and Impact
<!--Give the results and impact as shown below-->
The Disaster Response Dashboard provides emergency responders with critical, real-time insights, facilitating informed and timely decision-making. The system’s integration of social media data with visual analytics optimizes resource allocation, speeds up response time, and ultimately contributes to saving lives during crises. This project demonstrates the value of using AI and data visualization to enhance disaster resilience and response efforts.

## Articles published / References
[1]  S. R. Varghese, S. Juliet and J. Anitha, "Social Media Analytics for Disaster Management using BERT Model," 2023 International Conference on Emerging Research in Computational Science (ICERCS), Coimbatore, India, 2023, pp. 1-6, doi: 10.1109/ICERCS57948.2023.10434012.

[2]    M. A, G. S. S, R. SV and S. Juliet, "Sentimental Analysis from Social Media Post for        Disaster Management," 2023 International Conference on Circuit Power and Computing Technologies (ICCPCT), Kollam, India, 2023, pp. 469-474, doi: 10.1109/ICCPCT58313.2023.10245937.

[3]  D. Widodo, P. Kristalina, M. Z. S. Hadi and A. D. Kurniawati, "Performance Evaluation of Docker Containers for Disaster Management Dashboard Web Application," 2023 International Electronics Symposium (IES), Denpasar, Indonesia, 2023, pp. 551-556, doi: 10.1109/IES59143.2023.10242411.



