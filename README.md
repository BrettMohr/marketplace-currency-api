# Marketplace Currency API

<!-- TABLE OF CONTENTS -->

  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
  </ol>


<!-- ABOUT THE PROJECT -->

## About The Project

A simple currency conversion API built with Python and Flask

<!-- GETTING STARTED -->

## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

- Docker
- Postman

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/BrettMohr/marketplace-currency-api.git
   ```
2. CD into directory
   ```
   cd marketplace-currency-api
   ```
3. Build the project with docker
   ```sh
   docker-compose up
   ```
4. Import Postman Collection located in "./postman_collection" into Postman

   ```
   Postman: File > Import ...
   ```

<!-- USAGE EXAMPLES -->

## Usage

Once Docker is running the application, go to Postman and select an available endpoint in the collection and hit the SEND button to view the response.

The parameters required by the API are sent in the body.

## API Endpoints

### Get Currency Conversion

    GET /currency_convert

    Request Body
        {
            "origin_currency":"USD",
            "destination_currency": "EUR",
            "origin_value": 12.23
        }

    Response: Amount in origin_currency, converted to an amount in the destination_currency, along with original request
    Payload:
        {
            "destination_currency": "GBP",
            "destination_value": 8.78,
            "origin_currency": "USD",
            "origin_value": 12.23
        }

### Get Currency Rate

    GET /currency_rate

    Request Body
        {
            "origin_currency":"USD",
            "destination_currency": "GBP"
        }

    Response: Value of 1 unit of origin_currency in destination_currency, along with original request
    Payload:
        {
            "conversion_ratio": 0.7178201912914993,
            "destination_currency": "GBP",
            "origin_currency": "USD"
        }
