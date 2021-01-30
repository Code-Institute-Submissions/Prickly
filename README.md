
<h1 align="center">PRICKLY</h1>
<h1 align="center"><img src="" /></h1>

 <a href=""><img src="" width="25px" /></a> :point_left: Live website

  <a href="https://github.com/LigaMoon/Prickly"><img src="./readme_docs/githublogo.png" width="25px" /></a> :point_left: GitHub Repository
 
 # About



# Table of Contents

1. [User Experience (UX)](#user-experience)
    1. [Strategy Plane](#strategy-plane)
        1. [Business Goals](#business-goals)
        1. [User Stories](#user-stories)
    1. [Scope Plane](#scope-plane)
    1. [Structure Plane](#structure-plane)
    1. [Skeleton Plane](#skeleton-plane)
        - [Wireframes](#wireframes)

    1. [Surface Plane](#surface-plane)
        - [Color sheme](#color-scheme)
        - [Typography](#typography)
        - [Imagery](#imagery)
        - [Animations](#aniamations)
        - [Transitions](#transitions)

1. [Features](#features)
    1. [Existing Features](#existing-features)
        - [Common Features Accross Pages](#common-features-accross-pages)
        - [Features Specific to Pages](#features-specific-to-pages)
    1. [Future Features](#future-features)

1. [Information Architecture](#information-architecture)
    1. [Database](#database)
    1. [Structure](#structure)
    1. [Relationship](#relationship)

1. [Technologies Used](#technologies-used)
    1. [Languages](#languages)
    1. [Frameworks, Libraries and Programs](#frameworks,-libraries-and-programs)

1. [Testing](#testing)

1. [Deployment](#deployment)
    1. [Local](#local)
        - [Pre-requisites](#pre-requisites)
        - [Recommended](#recommended)
        - [Steps](#steps)
    1. [Remote](#remote)
        - [Pre-requisites](#pre-requisites)
        - [Steps](#steps)

1. [Credits](#credits)


# User Experience (UX)

## Strategy Plane
The main target audience for Prickly
- Age 15 - 35 as the product itself is filled with puns that might not be attractive to an older demographic.
- Users interested in cacti.
- Users interested in decorating their space.
- Users working with computers and interested in health benefits connected to cacti and computers.
- Users who don't feel discouraged by monthly subscription services.

The user can purchase individual items on the site which makes the site available to anyone visiting. However, due to the younger target audience, the main business model is subscription based to match up with multiple modern products. Each month users have the opportunity, based on their subscription value, to choosing new products that are delivered to them. This creates a fun aspect, inviting users to return and possibly purchase more products.

Research
- This is a B2C model, hence the website makes use of larger images/graphics and less text
- There are only a few cacti dedicated e-commerce sites, and none that I came across offering subscription services
- People purchasing items online are mostly impulse shopping and not many users like to register for new pages. This is why a subscription model is used to increase the number of returning users.

Features worth doing
- A Roadmap was used to identify which objectives are worth achieving. All objectives/high-level features were listed and scored on a 1-5 scale (5 being the most important) if they are Important or Viable. The importance score was summed together while the Viability scored was averaged and multiplied by the number of features. Since these numbers did not equal, they were plotted on the Importance/Viability graph to identify the most important ones and the ones that, for now, will be left out.

    <img src="./readme_docs/strategy-table.png"/>


    <img src="./readme_docs/strategy-chart.png"/>




### Business Goals
- Earn profit by allowing anyone to purchase products
- Connect the business to users to access a larger audience by having social media links accessible 
- Outperform competitors by providing excellent products, services, and customer support
- Provide unique designs by collaborating each month with a different artist on accessory designs




### User Stories

- #### Common user stories
    1. I want to easily navigate the site so that I can find what I'm looking for quickly.
    1. I want to be able to contact the company if I'm experiencing an issue.
    1. I want the website to be readable on all screen sizes.

    
- #### As a first-time visitor I want to
    1. Easily understand the purpose of the site so that I can decide whether I want to invest my time into it.
    1. Understand the benefits of becoming a member/registering for the site so that I can decide if I want to.
    1. View and compare all memberships so that I can decide what membership if any, I want to subscribe to.
    1. Easily find where I can register for the site so that I don't waste my time looking for it and I'm not discouraged not to sign up.
    1. Be able to quickly register and start using the site so that I can have my account and receive the benefits.

- #### As a casual shopper I want to
    1. Navigate to the shop page easily so that I can find what I need quickly.
    1. Filter all products by category so that I can quickly have oversight of the products that I'm interested in.
    1. Sort all items by date added, name or price so that I can identify new products, products that fit my budget, and find easier what I'm looking for.
    1. Search for an item from anywhere on the site so that I can easily find what I'm looking for.
    1. Be able to see the price of the item without clicking into it so that I can easily decide if I can afford the item.
    1. Be able to quickly add the item without having to click on the product so that I can save time if I know that I want to purchase the item.
    1. Be able to see more details about the product so that I can make an educated decision of whether to purchase the item.
    1. Select the quantity of the product so that I can choose how many products I'm purchasing and not have to add the same item multiple times.
    1. Be able to see the rating and reviews to allow me to judge if the item is worth the price based on other feedback.
    1. Leave a review so that I can provide my feedback and experience to the company and other shoppers.
    1. Edit my review so that I can change it in case I've changed my mind or made a mistake while adding the review.
    1. Delete my review so that I can remove it in case my review is no longer relevant or I don't want to keep it up.
    1. See my shopping cart as items are added to know how the total without having to go to another page.
    1. Edit the quantity of added items so that I don't have to remove and add items again.
    1. Remove added items easily so that I can purchase only the items that I want.
    1. See my shopping cart before checkout so that I can make changes before purchase.
    1. See all charges included before making a payment so that I can decide if I want to proceed with the purchase.
    1. View my order as I'm checking out to be able to confirm what I'm purchasing.
    1. easily add my details without too many steps so that I don't get discouraged by the lengthy checkout process.
    1. Securely add my payment information so that I feel safe giving my card details.
    1. See Order confirmation and receive confirmation e-mail so that I have proof of purchase and order number.


- #### As a member I want to
    1. Log in and sign out quickly and easily so that I can access or close my account.
    1. See my personal account information so that I can manage my details.
    1. See my membership site so that I can verify my benefits and the price of the membership.
    1. Change the membership easily so that I can control what benefits and expenses I'm having.
    1. Cancel paid membership so that I don't have to pay for it.
    1. See my order history so that I can have the confirmation and details for all of them in one place and manage them easily.
    1. Can see the estimated date of delivery so that I can arrange to receive the package.
    1. Recieve benefits as a member so that I get my money's worth.

- #### As an admin I want to
    1. Be able to add an item so that I can update the products on the site.
    1. Be able to edit and remove items so that I can customize items on the site and offer new deals to customers depending on the demand and new trends.
    1. Add and edit new memberships so that I can customize the price and benefits depending on the popularity of the membership.
    1. Add and edit new delivery types to accommodate shipping to more countries.
    1. Have oversight of the user data so that if anyone is experiencing an issue I can investigate and resolve the issue.


## Scope Plane
- MVP - Minimal Viable Product, additionally, what features are planned for this website

## Structure Plane
- How the information is logically grouped together

## Skeleton Plane
- Higher and lower priorities in a site, how the user will navihate towards those

- ### Wireframes
    - <details>
        <summary>Home</summary>
        <img src="./readme_docs/wireframes/Home.png"/>
    </details>

    - <details>
        <summary>Shop</summary>
        <img src="./readme_docs/wireframes/Shop.png"/>
    </details>
    
    - <details>
        <summary>Product</summary>
        <img src="./readme_docs/wireframes/Product.png"/>
    </details>

    - <details>
        <summary>Memberships</summary>
        <img src="./readme_docs/wireframes/Memberships.png"/>
    </details>

    - <details>
        <summary>Shopping Bag</summary>
        <img src="./readme_docs/wireframes/Shopping_Bag.png"/>
    </details>

    - <details>
        <summary>Checkout</summary>
        <img src="./readme_docs/wireframes/Checkout.png"/>
    </details>

    - <details>
        <summary>Order History</summary>
        <img src="./readme_docs/wireframes/Order_History.png"/>
    </details>

    - <details>
        <summary>Order Details</summary>
        <img src="./readme_docs/wireframes/Order_Details.png"/>
    </details>

    - <details>
        <summary>Register</summary>
        <img src="./readme_docs/wireframes/Register.png"/>
    </details>

    - <details>
        <summary>Log In</summary>
        <img src="./readme_docs/wireframes/Log_In.png"/>
    </details>

    - <details>
        <summary>My Details</summary>
        <img src="./readme_docs/wireframes/About_Me.png"/>
    </details>


## Surface Plane

- #### Color scheme
    - xxx

        <img src="./" height="100px" />
        <img src="./" height="50px" />

- #### Typography
    - xxx

        <img src="./" height="50px" />

- #### Imagery
    - Images
        - xxx

    - Graphics
        - xxx

- #### Other 
    - xxx


# Features

## Existing Features

### Common Features Across Pages
- [x] **Header** - facilitates an effortless navigation across all pages
    - xxx

### Features Specific to Pages
- [x] **Home** Page
    - xxx

## Future Features
- [ ] xxx


# Information Architecture

## Database
- xxx

## Structure
- xxx

## Relationship
- xxx


# Technologies Used

## Languages

## Frameworks, Libraries and Programs


# Testing

All testing was documented in [TESTING.md](https://github.com/LigaMoon/Prickly/blob/main/TESTING.md) file

<a href="https://github.com/LigaMoon/Prickly/blob/main/TESTING.md">   
:bar_chart: </a>  :point_left: testing.md



# Deployment

## Local
Instructions to run the project on your local device using an IDE

### Pre-requisites
- [Python 3](https://www.python.org/downloads/) - used to write the code and to run the project
- [PIP](https://pypi.org/project/pip/) - used to install packages
- [Git](https://git-scm.com/downloads) - used for version control
- [Visual Studio Code](https://code.visualstudio.com/) or any IDE of your choice - used to compile the code.
- [Stripe](https://stripe.com/en-ie) Account




### Recommended
- A virtual environment of your choice - used to contain all installations and packages and prevents clashing projects that might use the same package but different versions.
    - Python 3 has a built-in virtual environment [venv](https://docs.python.org/3/tutorial/venv.html). The commands might differ depending on your Operating System, it is advised to read the docs to ensure accuracy. To initialize on MacOS:

            python3 -m venv .venv
        where `.venv` is the name/path you are giving to the virtual environment

### Steps
1. Go to the project [repository](https://github.com/LigaMoon/Prickly)
1. Get the files used by using one of the methods below:
    - Download the files used by clicking the 'Code' button located in the top section of the repository. Then select 'Download ZIP' and unzip the files in the directory of your choice.

        <img src="./readme_docs/zip.png" height="200px" /> 
    
    - Clone the repository by running the following command from your IDE

            gh repo clone LigaMoon/Prickly
    
1. In your IDE, navigate to the project directory where you located downloaded files/cloned the repo

        cd path/to/your/folder
1. Activate your virtual environment. If using Python's venv:

        source .venv/bin/activate
    on MacOS and Unix where .venv is the name you gave previously

        .venv\Scripts\activate.bat
    on Windows where .venv is the name you gave previously

1. Install all reqauirements from [requirements.txt](requrements.txt) file
    
        pip3 install -r requirements.txt

1. Create a file `env.py` to store environment variables
1. Add environment variable in the format as shown below and also demonstrated in the [sample_env.py](sample_env.py) file

        os.environ.setdefault('SECRET_KEY', '<your-variable-goes-here>')
        os.environ.setdefault('DEVELOPMENT', '1')
        os.environ.setdefault('ALLOWED_HOSTS', '<your-variable-goes-here>')
        os.environ.setdefault('STRIPE_PUBLIC_KEY', '<your-variable-goes-here>')
        os.environ.setdefault('STRIPE_SECRET_KEY', '<your-variable-goes-here>')
        os.environ.setdefault('STRIPE_WH_SECRET', '<your-variable-goes-here>')
    where 
    -  `SECRET_KEY` value is a key of your choice, to ensure appropriate seccurity measures, this can be generated using [Django Secret Key Generator](https://miniwebtool.com/django-secret-key-generator/)
    -  `DEVELOPMENT` is set to `1` and is ised in settings.py logic to ensure file is dynamic between local and remote setups
    - `STRIPE_PUBLIC_KEY` and `STRIPE_SECRET_KEY` values are obatined from the [Stripe](https://stripe.com/en-ie) website
                <details>
                        <summary>How to get Stripe API values</summary>
                        <ul>
                            <li>Once logged in, you will be redirected to the **Overview** page, if not, navigate there by clicking **Overview** on the left hand side
                            </li>
                                <img src="./readme_docs/stripe-overview.png" height="200px">
                            <li>Get the API values by clicking on **Get your test API keys** as shown in the image above</li>
                            <li>Add Publishable key as `STRIPE_PUBLIC_KEY` and Secret key as `STRIPE_SECRET_KEY` environmental variable values</li>
                        </ul>
                </details>
    - `STRIPE_WH_SECRET` value is obtained from the [Stripe](https://stripe.com/en-ie) website in conjunction of using [ngrok](https://ngrok.com) to host the server
                    <details>
                        <summary>Getting Webhooks API value</summary>
                        <ul>
                            <li>Set up ngrok to generate a tunnel on your localhost port to use in Stripe webhooks later. Read on [ngrok](nhrok.com/downloads) website downloads page to learn how.</li>
                            <li>Go to your [stripe dashboard](dashboard.stripe.com) and naviagte to **Developers** > **Webhooks**
                            </li>
                            <li>Click **Add endpoint** and enter your ngrok link followed by `/checkout/wh/` as shown in the image below</li>
                                <img src="./readme_docs/stripe-endpoint.png" height="400px">
                            <li>Click on **recieve all events** and then Add endpoint to finish the setup</li>
                            <li>To get the `STRIPE_WH_SECRET` value, click on the added link under Endpoints and copy the Signing secret key in your variable</li>
                        </ul>
                </details>
    - `ALLOWED_HOSTS` this should be set to your ngrok url
1. Run the application

        python3 manage.py runserver

1. Website should be available on a link similar to `http://127.0.0.1:8000`. (check your IDE terminal)
1. Note: `python3` and `pip3` commands can vary depending on version/machine/IDE you're using. Always check docs if unsure.

## Remote
### Pre-requisites
- Set up [Heroku](https://dashboard.heroku.com/apps) Account and app
        <details>
            <summary>Heroku Basic Set Up</summary>
            <ul>
                <li>Register to the Heroku website by clicking on this [sign up link(https://signup.heroku.com/login)]</li>
                <li>Create a new app on the Heroku website, enter a unique name and choose a region closest to you.
                </li>
                    <img src="./readme_docs/new-app.png">
            </ul>
        </details>
- Create AWS account and upload static files used in the project
        <details>
            <summary>AWS S3 static file storage setup</summary>
            <ul>
                <li>Go to [aws.amazon.com](https://aws.amazon.com/) website and Register, you might have to enter your credit card details, however, while using free tier there should be no charges. That being said, you should monitor your own usage.</li>
                <li>After registration, go back to the [AWS](https://aws.amazon.com/) site and click the orange 'sign in to the Console' button.</li>
                <li>Sign in as 'Root User' with your e-mail address and password used in registration.</li>
                <li>At the top of the site, search for S3 and click on it to open.</li>
                <li>Click on the **Create bucket** button located on the top right.
                </li>
                <li>Name should match the Heroku app name, Region is set to the closest tot you, untick the 'Block all public access' and tick the acknowledgement next to the warning symbol.</li>
                <li>Go to the end and click **Create Bucket**</li>
                <li>To Enable static website hosting
                    <ul>
                        <li>Select the bucket by clicking on it and go to **Properties** located at the top.</li>
                        <li>Scroll down to the very bottom and click on 'Edit' under **Static website hosting**.</li>
                        <li>Select 'Enable' and enter the default values for Index document and Error document as these won't be used.
                        </li>
                            <img src="./readme_docs/aws-default-names.png">
                        <li>Click **Save changes**</li>
                    </ul>
                </li>
                <li>Make changes in Permissions
                    <ul>
                        <li>Go to **Permissions** located at the top</li>
                        <li>Scroll down and click 'Edit' under **Cross-origin resource sharing (CORS)** which will provide access between Heroku and the bucket</li>
                        <li>Scroll down to the very bottom and click on 'Edit' under **Static website hosting**.</li>
                        <li>Add the following JSON code (indent it properly) and save changes.
                            <pre>
                                [
                                    {
                                        "AllowedHeaders": [
                                            "Authorization"
                                        ],
                                        "AllowedMethods": [
                                            "GET"
                                        ],
                                        "AllowedOrigins": [
                                            "*"
                                        ],
                                        "ExposeHeaders": []
                                    }
                                ]
                            </pre>
                        </li>
                        <li>Click 'Edit' under **bucket policy** and click on 'Policy Generator' which will open in a new tab.</li>
                        <li>'Select Type or Policy' set to 'S3 Bucket Policy', 'Principal' set to '*', under 'Actions' add 'GetObject, GetObjectAcl, PutObject, PutObjectAcl, DeleteObject'</li>
                        <li>Go back to the previous tab and copy the **Bucket ARN** and paste it under **Amazon Resource Name (ARN)**
                        </li>
                            <img src="./readme_docs/aws-policy.png">
                        <li>Click 'Add Statement' and then click 'Generate Policy'.</li>
                        <li>Copy the code, paste it in the **bucket policy** field (previous tab) and add `/*` after the ARN to allow all resources in the bucket</li>
                        <li>Click 'Save Changes'.</li>
                        <li>Still in permissions click 'Edit' under **Access control list (ACL)**</li>
                        <li>Under 'Everyone', tick 'List'</li>
                        <li>Tick 'I understand the effects....' and Save changes.</li>
                    </ul>
                </li>
                <li>At the top search for **IAM** and click on it.</li>
                <li> Create a Group
                    <ul>
                        <li>On the left hand side, under 'Access management' click on **Groups**
                        </li>
                        <li>On the top right click 'Create New Group' and name it something that makes sense to you.</li>
                        <li>Click 'Next Step' and then 'Create Group' (skips the policy for now, we will create it in one of the following steps).</li>
                    </ul>
                </li>
                <li> Create a Policy
                    <ul>
                        <li>On the left hand side, under 'Access management' click on **Policies**.</li>
                        <li>On the top right click 'Create policy' select JSON and click on 'Import Managed Policy'.
                        </li>
                        <li>Search for 'S3', select **AmazonS3FullAccess** and click 'Import'.</li>
                        <li>Since we only want full access to our Bucket, go back to copy your ARN from before and add it under 'Resource' twice, the second time with `/*` after the ARN.
                            <img src="./readme_docs/policy-json.png" height="200px">
                        </li>
                        <li>Click on 'Review policy', add name and description and 'Create policy'.</li>
                    </ul>
                </li>
                <li> Attach the Policy to the Group created
                    <ul>
                        <li>Go to **Groups** on the left hand side.</li>
                        <li>Click on the relevant group and click on 'Attach Policy'.</li>
                        <li>Search for the policy just created, select it and click 'Attach Policy'.</li>
                    </ul>
                </li>
                <li> Create Users to put in the Group
                    <ul>
                        <li>Click on **Users** on the left hand side adn click 'Add user'.</li>
                        <li>Add name and tick to give 'Programmatic access', then click 'Next: Permissions'.</li>
                        <li>Select the group to put the user in and keep clicking 'Next; until the very end and click 'Create user'.</li>
                        <li>Click on 'Download .csv' file, this is important as you won't have access to it again!</li>
                        <li>Use the values from this file to later set your     `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` variables. </li>
                    </ul>
                </li>
        </details>


### Steps
1. In Heroku, go to **Resources** and search for **Heroku Postgres**, we will use this as our development database
    - Select 'Hobby Dev - Free' and click to Submit Order Form

1. Comment out the 'SQLite and Postgres databases' section in the `settings.py` file and uncomment 'Postgres Database' section. Add your `DATABASE_URL` link obtained from Heroku Config Vars

        DATABASES = {
            'default': dj_database_url.parse('your-url-goes-here')
        }
1. Migrate your models to Postgres SQL database

        python3 manage.py migrate

1. If you have a JSON file with products displayed on the site, import them now in this order

        python3 manage.py loaddata categories
        python3 manage.py loaddata products

1. Create a superuser that will be used to access the admin page as well as to manage the database. Enter username, password, and e-mail as required

        python3 manage.py createsuperuser

1. In `settings.py` delete the 'Postgres SQL Database' section (make sure you don't commit your DATABASE_URL link!) and un-comment 'SQLite and Postgres SQL Databases' section - this will allow for use of  either of the databases interchangeably

1. Freeze dependencies in a  requirements.txt file (if it hasn't been created/updated before)

        pip3 freeze --local > requirements.txt

1. Create a Procfile that tells Heroku to create a web dyno and add the following line in it, where `the-name-of-your-app` is the name of your django project

        web: gunicorn the-name-of-your-app.wsgi:application

1. `Add`, `commit` and `push` your changes up to GitHub

1. Go to Heroku and add all of the following environmental variables (Settings > Reveal Config Vars)

    | Key | Value |
    --- | ---
    AWS_ACCESS_KEY_ID | `<your_aws_access__key>`
    AWS_SECRET_ACCESS_KEY | `<your_aws_secret_access_key>`
    DATABASE_URL | `generated automatically`
    EMAIL_HOST_PASS | `<your_email_key>`
    EMAIL_HOST_USER | `<your_email>`
    SECRET_KEY | `<your_secret_key>`
    STRIPE_PUBLIC_KEY | `<your_stripe_public_key>`
    STRIPE_SECRET_KEY | `<your_stripe_secret_key>`
    STRIPE_WH_SECRET | `<your_stripe_webhook_key>`
    USE_AWS | `True`
    ALLOWED_HOSTS | `<your-heroku-app-url>`
    
1. In Heroku go to **Deploy** that's located at the top of the site

    <img src="./readme_docs/deploy.png" height="100px" /> 

1. Click on the **GitHub** option and connect your GitHub account as well as your repo from GitHub (search for the repo name)

    <img src="./readme_docs/heroku-github-connect.png" height="150px" />

1. Click on **Enable Automatic Deploys** and then **Deploy Branch**, you should see a successful build here

    <img src="./readme_docs/deploy-branch.png" height="200px" />

1. Open your app

    <img src="./readme_docs/open-app.png" height="70px" />

1. You should see `static/` folder with your static files in it in you S3 bucket.

1. In your S3 bucket, add `media/` folder.

1. If you didn't use JSON filer for product import, now is a good time to navigate to `your-ulr/admin/` page and add the Products and Categories in.

1. Your app should be deployed and you should be able to see your added products.


# Credits

### Code :floppy_disk:
- Collapsible sections in README.md seen on [GitHub Gist](https://gist.github.com/pierrejoubert73/902cc94d79424356a8d20be2b382e1ab) post done by pierrejoubert73



### Media :clapper:
- xxx


### Acknowledgements
- xxx
