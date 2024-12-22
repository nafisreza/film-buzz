# Testing

Navigate back to the [README.md](https://github.com/raycarter23/film-buzz/blob/main/README.md) file.

## Code Validation

### HTML

### CSS

### JavaScript

### Python

## Browser Compatibility

I tested my deployed project on all of the following browsers to check for compatibility and rendering issues.

| Browser   | Home Page                                                                                     | About Page                                                                                      | Blog Page                                                                                      | Notes |
|-----------|-----------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|-------|
| Chrome    | ![Chrome - Home - 1](/documentation/testing/browser-compatibility/chrome/chrome-bt-home-1.png) ![Chrome - Home - 2](/documentation/testing/browser-compatibility/chrome/chrome-bt-home-2.png)                                                   | ![Chrome - About - 1](/documentation/testing/browser-compatibility/chrome/chrome-bt-about-1.png) ![Chrome - About - 2](/documentation/testing/browser-compatibility/chrome/chrome-bt-about-2.png)                                                  | ![Chrome - Blog - 1](/documentation/testing/browser-compatibility/chrome/chrome-bt-blog-1.png) ![Chrome - Blog - 2](/documentation/testing/browser-compatibility/chrome/chrome-bt-blog-2.png)                                                   |  No issues detected, works as expected     |
| Firefox   | ![Firefox - Home - 1](/documentation/testing/browser-compatibility/firefox/firefox-bt-home-1.png) ![Firefox - Home - 2](/documentation/testing/browser-compatibility/firefox/firefox-bt-home-2.png)                                                 | ![Firefox - About - 1](/documentation/testing/browser-compatibility/firefox/firefox-bt-about-1.png) ![Firefox - About - 2](/documentation/testing/browser-compatibility/firefox/firefox-bt-about-2.png)                                                | ![Firefox - Blog - 1](/documentation/testing/browser-compatibility/firefox/firefox-bt-blog-1.png) ![Firefox - Blog - 2](/documentation/testing/browser-compatibility/firefox/firefox-bt-blog-2.png)                                                 |  Text rendering issues on homepage trending post section; Issue resolved by      |
| Safari    | ![Safari - Home - 1](/documentation/testing/browser-compatibility/safari/safari-bt-home-1.png) ![Safari - Home - 2](/documentation/testing/browser-compatibility/safari/safari-bt-home-2.png)                                                   | ![Safari - About - 1](/documentation/testing/browser-compatibility/safari/safari-bt-about-1.png) ![Safari - About - 2](/documentation/testing/browser-compatibility/safari/safari-bt-about-2.png)                                                  | ![Safari - Blog - 1](/documentation/testing/browser-compatibility/safari/safari-bt-blog-1.png) ![Safari - Blog - 2](/documentation/testing/browser-compatibility/safari/safari-bt-blog-2.png)                                                   |   No issues detected, works as expected    |
| Edge      | ![Edge - Home - 1](/documentation/testing/browser-compatibility/edge/edge-bt-home-1.png) ![Edge - Home - 2](/documentation/testing/browser-compatibility/edge/edge-bt-home-2.png)                                                       | ![Edge - About - 1](/documentation/testing/browser-compatibility/edge/edge-bt-about-1.png) ![Edge - About - 2](/documentation/testing/browser-compatibility/edge/edge-bt-about-2.png)                                                      | ![Edge - Blog - 1](/documentation/testing/browser-compatibility/edge/edge-bt-blog-1.png) ![Edge - Blog - 2](/documentation/testing/browser-compatibility/edge/edge-bt-blog-2.png)                                                       |   No issues detected, works as expected    |


## Responsiveness

I tested my deployed project across a variety of devices to ensure optimal responsiveness and a seamless user experience. Testing was done through a combination of Google Dev Tools and [Perfecto](https://www.perfecto.io/)

The results from these tests are shown in the table below:

| Device   | Screenshot | Notes |
|----------|------------|-------|
| Mobile   |   ![home-mbr](/documentation/testing/responsiveness/mobile/home-mbr.png) ![header-mbr](/documentation/testing/responsiveness/mobile/header-mbr.png) ![footer-mbr](/documentation/testing/responsiveness/mobile/footer-mbr.png) ![about-mbr1](/documentation/testing/responsiveness/mobile/about-mbr-1.png) ![about-mbr2](/documentation/testing/responsiveness/mobile/about-mbr-2.png) ![blogs-mbr1](/documentation/testing/responsiveness/mobile/blogs-mbr-1.png) ![blogs-mbr2](/documentation/testing/responsiveness/mobile/blogs-mbr-2.png) ![details-mbr](/documentation/testing/responsiveness/mobile/details-mbr.png) ![signup-mbr](/documentation/testing/responsiveness/mobile/signup-mbr.png) ![login-mbr](/documentation/testing/responsiveness/mobile/login-mbr.png) ![profile-mbr](/documentation/testing/responsiveness/mobile/profile-mbr.png) ![watchlist](/documentation/testing/responsiveness/mobile/watchlist-mbr.png)        |       |
| Tablet   |   ![home-tbr1](/documentation/testing/responsiveness/tablet/home-tbr1.png) ![home-tbr2](/documentation/testing/responsiveness/tablet/home-tbr2.png) ![header-tbr](/documentation/testing/responsiveness/tablet/header-tbr.png) ![footer-tbr](/documentation/testing/responsiveness/tablet/footer-tbr.png) ![about-tbr1](/documentation/testing/responsiveness/tablet/about-tbr1.png) ![about-tbr2](/documentation/testing/responsiveness/tablet/about-tbr2.png) ![blog-tbr1](/documentation/testing/responsiveness/tablet/blog-tbr1.png) ![blog-tbr2](/documentation/testing/responsiveness/tablet/blog-tbr2.png) ![details-tbr1](/documentation/testing/responsiveness/tablet/details-tbr1.png) ![details-tbr2](/documentation/testing/responsiveness/tablet/details-tbr2.png) ![signup-tbr](/documentation/testing/responsiveness/tablet/signup-tbr.png) ![login-tbr](/documentation/testing/responsiveness/tablet/login-tbr.png) ![profile-tbr](/documentation/testing/responsiveness/tablet/profile-tbr.png) ![watchlist-tbr](/documentation/testing/responsiveness/tablet/watchlist-tbr.png)        |       |
| Desktop  |   ![home-dtr](/documentation/testing/responsiveness/desktop/home-dtr.png) ![footer-dtr](/documentation/testing/responsiveness/desktop/footer-dtr.png) ![about-dtr1](/documentation/testing/responsiveness/desktop/about-dtr1.png) ![about-dtr2](/documentation/testing/responsiveness/desktop/about-dtr2.png) ![blog-dtr1](/documentation/testing/responsiveness/desktop/blog-dtr1.png) ![blog-dtr2](/documentation/testing/responsiveness/desktop/blog-dtr2.png) ![details-dtr1](/documentation/testing/responsiveness/desktop/details-dtr1.png) ![details-dtr2](/documentation/testing/responsiveness/desktop/details-dtr2.png) ![signup-dtr](/documentation/testing/responsiveness/desktop/signup-dtr.png) ![login-dtr](/documentation/testing/responsiveness/desktop/login-dtr.png) ![profile-dtr](/documentation/testing/responsiveness/desktop/profile-dtr.png) ![watchlist-dtr](/documentation/testing/responsiveness/desktop/watchlist-dtr.png)         |       |



## Lighthouse Audit

To ensure optimal performance, accessibility, and user experience, I conducted a thorough Lighthouse audit on all key pages of the Film Buzz project. Both desktop and mobile versions were rigorously tested, yielding impressive results that showcased high levels of responsiveness and usability. With most performance scores exceeding 70, the site demonstrated strong overall efficiency. Accessibility scores also saw significant improvement after the addition of ARIA labels to key link tags, enhancing navigation for users relying on assistive technologies.

The audit identified several opportunities for optimisation, including reducing the Largest Contentful Paint time, eliminating render-blocking resources, properly sizing images, and implementing more efficient caching policies. Additional recommendations involved serving images in next-gen formats, minimising unused CSS and JavaScript, and improving text compression. While these findings present valuable opportunities for further enhancing performance, no critical issues were identified, affirming the site’s reliability and user-friendliness.

These audits confirm that the Film Buzz website delivers a seamless and efficient experience across devices, achieving a balance between performance, accessibility, and user satisfaction. The table below summarises the audit results for each page, complete with screenshots for reference.

| Page              | Size     | Screenshot | Notes |
|-------------------|----------|------------|-------|
| Home              | Desktop  |     ![home-desktop](/documentation/testing/light-house-audit/home-lh-desktop.png)       |   Some minor warnings    |
| Home              | Mobile   |     ![home-mobile](/documentation/testing/light-house-audit/home-lh-mobile.png)       |   Some minor warnings    |
| About             | Desktop  |     ![about-desktop](/documentation/testing/light-house-audit/about-lh-desktop.png)        |  Some minor warnings     |
| About             | Mobile   |     ![about-mobile](/documentation/testing/light-house-audit/about-lh-mobile.png)      |   Some minor warnings    |
| Blog              | Desktop  |     ![blog-desktop](/documentation/testing/light-house-audit/blog-lh-desktop.png)       |    No major warnings   |
| Blog              | Mobile   |     ![blog-mobile](/documentation/testing/light-house-audit/blog-lh-mobile.png)       |   Some minor warnings    |
| Details           | Desktop  |     ![details-desktop](/documentation/testing/light-house-audit/details-lh-desktop.png)       |  No major warnings     |
| Details           | Mobile   |     ![details-mobile](/documentation/testing/light-house-audit/details-lh-mobile.png)       |   Some minor warnings    |
| Login             | Desktop  |     ![login-desktop](/documentation/testing/light-house-audit/login-lh-desktop.png)       |  Some minor warnings    |
| Login             | Mobile   |      ![login-mobile](/documentation/testing/light-house-audit/login-lh-mobile.png)      |   Some minor warnings    |
| Sign Up           | Desktop  |      ![signup-desktop](/documentation/testing/light-house-audit/signup-lh-desktop.png)      |  No major warnings     |
| Sign Up           | Mobile   |      ![signup-mobile](/documentation/testing/light-house-audit/signup-lh-mobile.png)      |  Some minor warnings     |
| Profile           | Desktop  |    ![profile-desktop](/documentation/testing/light-house-audit/profile-lh-desktop.png)        |  Some minor warnings     |
| Profile           | Mobile   |    ![profile-mobile](/documentation/testing/light-house-audit/profile-lh-mobile.png)       |  Some minor warnings     |
| Watchlist         | Desktop  |     ![watchlist-desktop](/documentation/testing/light-house-audit/watchlist-lh-desktop.png)       |  Some minor warnings     |
| Watchlist         | Mobile   |     ![watchlist-mobile](/documentation/testing/light-house-audit/watchlist-lh-mobile.png)       |  Some minor warnings     |
| Search Results    | Desktop  |     ![search-desktop](/documentation/testing/light-house-audit/searchresults-lh-desktop.png)       |  No major warnings     |
| Search Results    | Mobile   |     ![search-mobile](/documentation/testing/light-house-audit/searchresults-lh-mobile.png)       |  Some minor warnings     |
| Not Found Page    | Desktop  |     ![notfound-desktop](/documentation/testing/light-house-audit/notfound-lh-desktop.png)       |  Some minor warnings     |
| Not Found Page    | Mobile   |      ![notfound-mobile](/documentation/testing/light-house-audit/notfound-lh-mobile.png)      |  Some minor warnings     |


## Defensive Programming

Defensive programming was manually tested with the below user acceptance testing:

| Page | User Action | Expected Result | Pass/Fail | Comments |
| --- | --- | --- | --- | --- |
| **Home Page** | | | | |
| | Clicking on logo | Redirection to Home page | Pass | |
| | Navbar links | Go to different pages of the site | Pass | |
| | Explore more button | Redirect to the blog page | Pass | |
| | Click on any category | Loads the posts for a specific category only | |
| | Click on any recent comment | Redirects to the post where the comment has been added | Pass | Most recent 3 comments are shown |
| | Footer Social Links | Visit social media profiles | Pass | |
| **About Page** | | | | |
| | Click on any FAQ | Expands the accordion with the answer of the question | Pass | |
| **Sign Up** | | | | |
| | Click on Sign Up button on home page | Redirection to Sign Up page | Pass | |
| | Enter unique username | Field will only accept username | Pass | Must be unique |
| | Enter valid email address | Field will only accept email address format | Pass | Match with email patterns |
| | Enter valid password (twice) | Field will only accept password format | Pass | Must be a strong password |
| | Click Sign Up button | Redirects user to feed | Pass | |
| | Already have an account button | Redirects to login page | Pass | |
| **Log In** | | | | |
| | Click on the Login button on home page | Redirection to Login page | Pass | |
| | Enter valid username | Field will only accept email address format | Pass | |
| | Enter valid password | Field will only accept password format | Pass | |
| | Click Login button | Redirects user to feed | Pass | |
| | Don't have an account button | Redirects to sign up page | Pass | |
| **Log Out** | | | | |
| | Click Logout button | Redirects user to home page | Pass | User must be logged in first |
| **Own Profile** | | | | |
| | Click on Profile button in nav | User will be redirected to their Profile page | Pass | Shows user's information |
| | Click on Edit Profile button | User will be redirected to the edit profile page | Pass | |
| | Click on Save button | User info will be updated | Pass | |
| | My posts section | User will be shown his/her own posts | Pass | |
| | Create Post button | Loads post creation page where user can make a new post | Pass | |
| | Go to watchlist button | Redirects to user's watchlist page | Pass | |
| **Blog Page** | | | | |
| | Click on featured post | Loads the post details of the particular featured post | Most recent post is set as featured post |
| | Click on any recent post | Loads the post details of the particular recent post | Most recent post are shown except the first one |
| | Click on next/prev button on pagination | Goes to the next or previous page of the blog | Supports dynamic pagination based on number of posts |
| | Click on any category | Loads the posts for a specific category only | |
| **Individual Post Page** | | | | |
| | Click delete icon on own post | User is redirected to post delete confirmation page | Pass | |
| | Brute forcing the URL to delete another user's post | User should be given an error as he is not the owner of the post | Pass | Redirects user to error page |
| | Type text into Leave Your Comment form and click Send | Comment is created under current post | Pass | |
| **Edit Post Page** | | | | |
| | Click on the Edit button | Post will be loaded as editor mode | Pass | |
| | Click on the Save button | User will be redirected to the original post with updated data | Pass | |
| **Delete Post Page** | | | | |
| | Click on the Delete button | Post will be permanently deleted | Pass | |
| | Click on the Cancel button | User will be redirected to the original post | Pass | |
| **Comments** | | | | |
| | Click Edit icon on own comment | User is redirected to edit comment page | Pass | |
| | Click delete button on own comment | The particular comment of the user is deleted | Pass | |
| | Brute forcing the URL to delete another user's comment if not on your post | User should be given an error | Pass | Redirects user to error page |
| | Brute forcing the URL to edit another user's comment | User should be given an error | Pass | Redirects user to error page |
| **Edit Comment Page** | | | | |
| | Make changes in the comment form and click submit | Original comment will be updated | Pass | |
| | Click on the Cancel button | User will be redirected to the original post | Pass | |
| **Delete Comment Page** | | | | |
| | Click on the Delete button | Comment will be permanently deleted | Pass | |
| | Click on the Cancel button | User will be redirected to the original post | Pass | |
| **Watchlist Page** | | | | |
| | Search movie name into search box | User will be redirected to the search-results page | Pass | Fetches movie details from TMDB API based on query |
| | Click delete icon on any movie card | The particular movie will be deleted from the watchlist | Pass | |
| **Search Posts** | | | | |
| | Type text into search form into nav and click the search icon | User is directed to a page with posts containing their search query | Pass | If there are no posts containing the query the page will let the user know there was no results for their query |
| | Click on any post | User will be redirected to the particular post | Pass | |
| **Error Page** | | | | |
| | Click on Back To Home button | User will be redirected to their feed | Pass | |
| **Admin Panel** | | | | |
| | Brute forcing the URL to access Admin Panel as a regular user | User should be given an error | Pass | Redirects user to error page |
| | Click delete icon on post | Admin is redirected to post delete confirmation page | Pass | Admin's are able to delete any post on the site regardless of if they are the author or not |
| | Click edit icon on post | Admin is redirected to post edit page | Pass | Admin's are able to change any post on the site regardless of if they are the author or not |
| | Add categories | Admins can create more movie categories for the blog | Pass | Regular users are only allowed to select a category from available options |

## User Story Testing

Below are all of my implemented user stories, with accompanying screenshots to demonstrate their functionality and how they meet the project requirements.

| ID  | User Story                                                                                  | Implementation |
|-----|---------------------------------------------------------------------------------------------|----------------|
| 1   | As a first-time site visitor, I can clearly see the website's purpose so that I can use it in the future. | [Website's Purpose]()           |
| 2   | As a developer, I can get an idea of the whole design system so that I can work on the UI/UX design.       | ![Whole Design System-1](/documentation/testing/user-story-testing/lf-desktop.png) ![Whole Design System-2](/documentation/testing/user-story-testing/lf-tablet.png) ![Whole Design System-3](/documentation/testing/user-story-testing/lf-mobile.png)           |
| 3   | As a developer, I can get an idea of which components to build so that I can work on the design system.    | ![Design System Components-1](/documentation/testing/user-story-testing/design-components.png) ![Design System Components-2](/documentation/testing/user-story-testing/wireframing-website.png)          |
| 4   | As a developer, I can build the pages based on the Figma designs so that I can check how the website looks in real time. | [Figma Designs]()           |
| 5   | As a user, I can create an account so that I can make my profile.                                         | ![Create an account-1](/documentation/testing/user-story-testing/create-an-account-1.png) ![Create an account-2](/documentation/testing/user-story-testing/create-an-account-2.png) ![Create an account-3](/documentation/testing/user-story-testing/create-an-account-3.png)           |
| 6   | As a registered user, I can log in to my account so that I can access the site.                           | ![Login to account-1](/documentation/testing/user-story-testing/login-1.png) ![Login to account-2](/documentation/testing/user-story-testing/login-2.png) ![Login to account-3](/documentation/testing/user-story-testing/login-3.png)     |
| 7   | As a registered user, I can log out of my account so that I can delete the session on my current device.  | ![Log out of account-1](/documentation/testing/user-story-testing/logout-1.png) ![Log out of account-2](/documentation/testing/user-story-testing/logout-2.png)          |
| 8   | As a registered user, I can update my profile information so that other users can identify me.           | ![Update my profile-1](/documentation/testing/user-story-testing/update-profile-1.png) ![Update my profile-2](/documentation/testing/user-story-testing/update-profile-2.png) ![Update my profile-3](/documentation/testing/user-story-testing/update-profile-3.png)          |
| 9   | As a registered user, I can create posts so that I can share my thoughts about different movies.          | ![Create Posts-1](/documentation/testing/user-story-testing/create-post-1.png) ![Create Posts-2a](/documentation/testing/user-story-testing/create-post-2a.png) ![Create Posts-2b](/documentation/testing/user-story-testing/create-post-2b.png) ![Create Posts-3](/documentation/testing/user-story-testing/create-post-3.png)           |
| 10  | As an author, I can edit my posts so that I can correct information in the future.                        | ![Edit Posts-1](/documentation/testing/user-story-testing/edit-post-1.png) ![Edit Posts-2](/documentation/testing/user-story-testing/edit-post-2.png) ![Edit Posts-3](/documentation/testing/user-story-testing/edit-post-3.png)           |
| 11  | As an author, I can delete my posts so that I can remove content that I no longer want to be published.   | [Delete Posts]()           |
| 12  | As a user, I can view all the posts so that I can learn about different movies.                           | [View all Posts]()           |
| 13  | As a registered user, I can comment on other users' posts so that I can engage with them in a discussion. | [Comment on other posts]()           |
| 14  | As a commenter, I can edit my existing comments so that I can correct information.                        | [Edit my Comments]()           |
| 15  | As a commenter, I can delete existing comments so that I can remove my opinions.                         | [Delete my Comments]()           |
| 16  | As a user, I can filter posts so that I can view posts of a specific movie genre.                         | [Filter Posts]()           |
| 17  | As a user, I can search posts so that I can filter posts based on titles.                                 | [Search Posts]()           |
| 18  | As a registered user, I can create, update, and delete my own watchlist so that I can track movies I am interested in watching. | ![Create Watchlist-1](/documentation/testing/user-story-testing/create-watchlist-1.png) ![Create Watchlist-2](/documentation/testing/user-story-testing/create-watchlist-2.png) ![Create Watchlist-3](/documentation/testing/user-story-testing/create-watchlist-3.png) ![Create Watchlist-4](/documentation/testing/user-story-testing/create-watchlist-4.png) ![Create Watchlist-5](/documentation/testing/user-story-testing/create-watchlist-5.png) ![Update Watchlist-1](/documentation/testing/user-story-testing/update-watchlist-1.png) ![Update Watchlist-2](/documentation/testing/user-story-testing/update-watchlist-2.png) ![Delete Watchlist-1](/documentation/testing/user-story-testing/delete-watchlist-1.png) ![Delete Watchlist-2](/documentation/testing/user-story-testing/delete-watchlist-2.png) ![Delete Watchlist-3](/documentation/testing/user-story-testing/delete-watchlist-3.png)         |
| [19]  | As a site visitor/user, I can easily navigate the site on any device so that I have a seamless experience whether on desktop or mobile. | For detailed information on the successful implementation of this user story, please refer to the [Responsive Navigation](#responsiveness) section            |
| 20  | As an admin, I can add, edit, or delete posts so that the database remains accurate.                      | [Admin - add, edit, or delete posts]()           |



## Python Unit Testing

## Bugs

### Fixed Bugs

| **Bug**                          | **Location**                          | **Cause**                                                                                                                                     | **Solution / Fix**                                                                                                                                                             |
|------------------------------------|---------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Environment variable not loading  | `settings.py` and `.env`             | Environment variables defined in `.env` were not being loaded into the project, likely due to missing or incorrect package usage.             | Fixed using `python-dotenv` package.                                                                                                                                          |
| Cloudinary Images not loading     | Media files (e.g., `/media/`)         | Cloudinary was not correctly syncing media files between the cloud and the local host, likely due to missing configurations or unsynced media directory. | Fixed by ensuring that the Cloudinary storage backend was properly configured in `settings.py` and syncing both media directories (local and cloud) to match.                 |
| Missing movies App dependency     | `watchlist/models.py`                 | The `Watchlist` model attempted to import the `Movie` model from a movies app that did not exist in the project, resulting in a `ModuleNotFoundError`. | Fixed by creating a `movies` app to define the `Movie` model.                                                                                                                |
| Comma Error in `INSTALLED_APPS`   | `settings.py` (`INSTALLED_APPS`)      | A missing comma after `'watchlist.apps.WatchlistConfig'` caused Django to concatenate the next entry (`'cloudinary'`), leading to an `ImportError`. | Fixed by adding a missing comma after `'watchlist.apps.WatchlistConfig'`.                                                                                                    |
| Duplicate slug causing IntegrityError | Watchlist `save` method             | The `slug` field was not dynamically ensuring uniqueness, causing an `IntegrityError` when duplicate slugs were generated.                   | Updated the `save` method to dynamically generate unique slugs by appending a counter to the base slug if a conflict is detected.                                             |
| Categories Not Displaying in Dropdown | Admin Panel: Blog > Posts > Add Post | No category instances existed in the database, causing the dropdown for categories to be empty.                                              | Manually added the predefined categories using the Categories section in the admin panel.                                                                                     |
| Comment not submitting to the database | `views.py`                         | Not linking Django form with `details.html`.                                                                                                 | Fixed by using `form.as_p` in `details.html` instead of `textarea`.                                                                                                          |
| CKEditor not loading              | `base.html`                           | CKEditor extra CSS and JavaScript files were not loading.                                                                                     | Used Jinja block templates to define `extra_css` and `extra_js`. Found the solution through [Reddit r/django](https://www.reddit.com/r/django/comments/6z38c1/help_with_adding_javascript_to_django_templates/).                                                                 |
| List bullet points not displaying | `about.html`                          | Tailwind CSS overrides the default list style, so bullet points were not visible by default.                                                  | Added the `list-disc` class to the `<ul>` element to explicitly set the bullet points. Reference: [Tailwind CSS Docs - List Style Type](https://tailwindcss.com/docs/list-style-type). |


### Unfixed Bugs

All identified bugs have been resolved, and no outstanding bugs need to be addressed.

