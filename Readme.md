Data Source:
For this application, I used http://books.toscrape.com — a publicly available website designed for practicing web scraping. It lists books along with their titles, prices, and ratings, which made it suitable for demonstrating scraping, data processing, and admin dashboard integration.

Implementation Flow:

Web Scraper:

Built using Python and BeautifulSoup.

A function (scrape_books()) extracts book titles, prices, and ratings from the website.

This script is triggered manually through a "Scrape Now" button on the admin panel.

Backend:

Developed using Flask (Python framework).

Includes routes for login authentication, dashboard rendering, and triggering the scraper.

Uses a dummy login (admin / admin123) for accessing the admin panel.

Frontend:

Created using HTML and CSS.

Includes a basic login page and a dashboard with a paginated table showing scraped data.

Database:

Used MongoDB Atlas (cloud-hosted NoSQL database).

Data is inserted into a collection (books) under the database (scraperDB).

Old data is cleared before inserting fresh records on every scrape.

Deployment:

The complete application (frontend + backend) is deployed on Render.com.

Environment variables (e.g., MONGO_URI) are securely stored in Render’s environment settings.

This setup demonstrates my ability to integrate web scraping, backend development, cloud-hosted databases and cloud deployment using modern full-stack development practices.