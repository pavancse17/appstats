# App Stats API
###  Setting up the app:
1. Download and extract this <a href="https://github.com/pavancse17/appstats/archive/master.zip">repository</a>.</li>
2. Setup environment with Python 3.7.4</li>
3. Navigate to root folder and install all dependencies: `pip3 install -r requirements.txt`
4. Navigate inside the folder `adjust` where you will find `manage.py` file.
5. Migrate schemas: `./manage.py migrate`.
7. Insert [sample data](https://gist.github.com/kotik/3baa5f53997cce85cc0336cb1256ba8b/) to DB using management command provided: `./manage.py write_dataset`.
8. Run the dev server `./manage.py runserver`.
9. Now you can use the API in the browser using `http://localhost:8000/app-stats/`

### API Usage:
1. Exposed query params for searching or filtering data:
   * `date_from` - To get data from the date passed.
   * `date_to` - To get data upto the date passed.(Use both date_from and date_to to get data between the interval.)
   * `date` - To get the data for the exact date matched.
   * Valid query parms: `os`, `channel`, `country`, `impressions`, `clicks`, `installs`, `spend`, `revenue`, `cpi` to search for the matched data.

2. Exposed query_parm for sorting.
   * All fields exposed for the searching functionality except `date_from` and `date_to` are available for sorting.
   * To sort the data with required field, You need to follow the pattern:
      * `o=<field_name>` for ascending order, 
      * `o=-<field_name>` for descending order.
3. Exposed query_param for grouping the data.
   * Use `group_by` query_parm to group data with xone or more valid fields.
   * Valid fields for grouping: `date`, `channel`, `country`, `os`.
     * Pattern: 
       * To group by single field `group_by=<field_name>`.
       * To group by multiple fields `group_by=<field_name1>&group_by=<field_name2>`.

### Endpoints with few use cases:
1. Show the number of impressions and clicks that occurred before the 1st of June 2017, broken down by channel and country, sorted by clicks in descending order.
    ```
    /app-stats/?date_to=2017-06-01&group_by=channel&group_by=country&o=-clicks
    ```
2. Show the number of installs that occurred in May of 2017 on iOS, broken down by date, sorted by date in ascending order.
    ```
    /app-stats/?date_from=2017-05-01&date_to=2017-05-31&os=ios&group_by=date&o=date
    ```
3. Show revenue, earned on June 1, 2017 in US, broken down by operating system and sorted by revenue in descending order.
    ```
    /app-stats/?date=2017-06-01&country=US&group_by=os&o=-revenue
    ```
4. Show CPI and spend for Canada (CA) broken down by channel ordered by CPI in descending order.
    ```
    /app-stats/?country=CA&group_by=channel&o=-cpi
    ```



