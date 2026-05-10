# Leadership Self Assessment

A full-stack self assessment web application built using Django that allows users to evaluate leadership and personal development skills through a structured questionnaire system. The application calculates scores dynamically, displays results instantly, and sends a detailed email report with a downloadable PDF attachment.

---

# Project Structure

The project follows Django’s modular architecture for better maintainability and scalability.

## Main Components

- **Templates**  
  Contains all frontend HTML pages such as:
  - Assessment form
  - Result page
  - Email template
  - PDF template

- **Static Files**  
  Includes CSS used for UI styling and responsiveness.

- **Views**  
  Handles:
  - Form submission
  - Score calculation
  - Result generation
  - Email sending
  - PDF generation

- **Models**  
  Stores questionnaire and user response data.

- **Utilities / Services**  
  Dedicated logic for:
  - Email handling
  - PDF generation using WeasyPrint

This structure keeps business logic separated from presentation logic and improves code readability.

---

# Scoring Logic

The assessment consists of multiple questions where users select predefined options mapped to numerical scores.

## Flow

1. User submits assessment form
2. Each selected option contributes a score
3. Scores are summed dynamically
4. Final score is categorized into assessment levels
5. Results are displayed and emailed to the user

## Example

| Option | Score |
|--------|--------|
| Strongly Agree | 5 |
| Agree | 4 |
| Neutral | 3 |
| Disagree | 2 |
| Strongly Disagree | 1 |

The final score determines the user’s performance category or leadership evaluation level.

---

# Email Service Choice

The project uses the Brevo Email API for transactional email delivery instead of traditional SMTP integration.
## Why Brevo API?

- SFaster and more reliable than standard SMTP connections
- Better email delivery and monitoring support
- Secure API-based authentication
- Easier scalability for production deployments
- Reduced chances of authentication and SMTP-related failures

The Brevo API is used to:
- Send assessment confirmation emails
- Deliver final assessment results
- Attach generated PDF reports to emails

Sensitive credentials such as the Brevo API key are securely managed using environment variables (.env) to avoid exposing secrets in the codebase.

---

# PDF Generation

PDF reports are generated using **WeasyPrint**.

## Why WeasyPrint?

- Excellent HTML/CSS rendering support
- Cleaner PDF styling compared to basic PDF libraries
- Easy conversion from existing email/report templates
- Works well with Django template rendering

The generated PDF contains:
- User responses
- Final score
- Assessment summary

---

# AI Assistance Usage

AI tools were used as a development support assistant for:

- Debugging Django and frontend issues
- Improving UI design and responsiveness
- Generating and refining CSS layouts
- Assisting with PDF generation integration
- Understanding deployment configurations
- Improving code structure and documentation

All final implementation, integration, and project customization were manually developed and tested.
