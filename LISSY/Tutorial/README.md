# LISSY

## What is LISSY?

LISSY is a remote-execution system that allows researchers to access [LIS](https://www.lisdatacenter.org/) and [LWS](https://www.lisdatacenter.org/data-access/lws/) microdata from a remote location while adhering to the privacy restrictions mandated by the countries providing the data. It offers secure access to the microdata through a web-based [Job Submission Interface](https://www.lisdatacenter.org/data-access/lissy/syntax/).

## How to Register for LISSY?

[LIS](https://www.lisdatacenter.org/) grants access to its micro-databases to registered users for a period of one year, renewable annually.

[Register for access to LISSY](https://www.lisdatacenter.org/data-access/lissy/)

## How to Get Started with LISSY?

Users write and submit statistical programs written in [R](https://www.r-project.org/), [SAS](https://www.sas.com/), [SPSS](https://www.ibm.com/products/spss-statistics), or [Stata](https://www.stata.com/) through the [LISSY interface](https://www.lisdatacenter.org/data-access/lissy/) (Batch coding mode). LISSY automatically processes the jobs and typically returns aggregated results to users within a few minutes.

To ensure proper processing of user requests, LISSY requires a few exceptions to the standard statistical program syntax.

- Detailed documentation on the LIS/LWS Databases can be found online through METIS: \
[http://www.lisdatacenter.org/frontend](http://www.lisdatacenter.org/frontend)

- To get acquainted with the LIS data, please have a look at our self-teaching materials: \
[http://www.lisdatacenter.org/resources/self-teaching/](http://www.lisdatacenter.org/resources/self-teaching/)

- Check out our FAQ to see if your questions are addressed there: \
[http://www.lisdatacenter.org/resources/faq/](http://www.lisdatacenter.org/resources/faq/)

- For remaining questions, feel free to contact our user support: \
[usersupport@lisdatacenter.org](usersupport@lisdatacenter.org)




## LIS’ Rules for Citation


All papers that use LIS microdata must be submitted for inclusion in the LIS Working Paper series before they are published in books, journals or other venues. Please look for further information on our General Policies and Practices webpage: [http://www.lisdatacenter.org/working-papers/#general](http://www.lisdatacenter.org/working-papers/#general)

[Privacy Policy](https://www.lisdatacenter.org/about-lis/terms-of-use/)

Users of the [LIS](https://www.lisdatacenter.org/) or [LWS](https://www.lisdatacenter.org/data-access/lws/) microdata are required to cite the data source in their list of references. As recommended by the [Chicago Manual of Style](https://www.chicagomanualofstyle.org/) (15th edition, 2007, pp. 753-754, 17.358), LIS requests that authors use the following format.

# Job Submission

## Submit Jobs through LISSY Web-Based Interface

Once connected to [LISSY](https://www.lisdatacenter.org/data-access/lissy/) through the web-based interface with the userid and password received during the registration process, you can:

- Write and submit statistical requests in [R](https://www.r-project.org/), [SAS](https://www.sas.com/), [SPSS](https://www.ibm.com/products/spss-statistics), and [Stata](https://www.stata.com/) (Job Session Pane).
- Track job status and view both job request and resulting listing (Recent Jobs Pane).
- Manage (view, clean, and search) all job requests you ever sent (Job Archive Pane).

Note that, for security reasons, the output of all job requests will be returned to the email registered in [LISSY](https://www.lisdatacenter.org/data-access/lissy/).

To ensure proper processing of user requests, [LISSY](https://www.lisdatacenter.org/data-access/lissy/) requires a few exceptions to the usual statistical program syntax. If you are not familiar with statistical package coding, first visit our [Get Started with LISSY](https://www.lisdatacenter.org/data-access/lissy/) section.

## Dataset Aliases

A [LIS](https://www.lisdatacenter.org/) (or [LWS](https://www.lisdatacenter.org/data-access/lws/)) dataset refers to harmonised microdata for one country and one year and consists of two datafiles: one household-level file and one individual-level file including their respective household members. Some [LWS](https://www.lisdatacenter.org/data-access/lws/) datasets include a household-level replicate weights file. Instead of using file names, datafiles are referred to by short aliases, constructed as follows:

- The concatenation of the 2-digit [3166 ISO country code](https://www.iso.org/iso-3166-country-codes.html) with the last 2 digits of the dataset reference year.
- A letter used to identify the specific type of dataset within each database.

| Database   | Database Type           | Letter Code |
|------------|-------------------------|-------------|
| LIS        | Household File          | h           |
|            | Person File             | p           |
| LWS        | Household File          | h           |
|            | Person File             | p           |
|            | Implicate File*         | r           |
| ERFLIS     | Household File          | h           |
|            | Person File             | p           |

As an example, Luxembourg 2004 household-level [LIS](https://www.lisdatacenter.org/) (or [LWS](https://www.lisdatacenter.org/data-access/lws/)) datafile is identified by the same alias `lu04h`.

* For more information about the Implicate File that contains replicate weights, consult the [LWS User Guide](https://www.lisdatacenter.org/data-access/lws/).

## Datafile Calling by Statistical Package

In all statistical packages, calling a datafile requires referring to its complete filename, which generally consists of a path, a name, and an extension. In [LISSY](https://www.lisdatacenter.org/data-access/lissy/), specific syntax – by statistical package – is used to call a dataset file based on its alias. As an example, calling Luxembourg 2010 Household file (alias `lu10h`):

| Statistical Package | How to Call a Data File | Syntax Example |
|--------------------|-------------------------|----------------|
| R                  | Pass the alias as a string to a special function `read.LIS` | `ds <- read.LIS("lu10h");` <br> Alternatively, you can use the [lissyrtools](https://github.com/lisdatacenter/lissyrtools) package: <br> `library(lissyrtools)` |
| SAS                | Place the `&` character before the alias | `PROC MEANS DATA=&lu10h;` |
| SPSS               | Use the alias with no prefix | `get file = lu10h` |
| Stata              | Place the `$` character before the alias | `use $lu10h` <br> Alternatively, you can use the `lissyuse` command: <br> `lissyuse [, options ]` |

* This function has additional parameters for user convenience. Due to [LIS](https://www.lisdatacenter.org/) security procedures, the syntax for generating output with [R](https://www.r-project.org/) in [LISSY](https://www.lisdatacenter.org/data-access/lissy/) is slightly modified. [Click here](https://www.lisdatacenter.org/data-access/lissy/) for detailed information.

## Producing Graphs by Statistical Package

In [LISSY](https://www.lisdatacenter.org/data-access/lissy/), specific syntax is used in combination with the syntax of each graph – by statistical package – to allow users to display their graphs on the Web-based [Job Submission Interface](https://www.lisdatacenter.org/data-access/lissy/) and download them in PNG format. See the below example for producing a simple twoway graph; the parts of the syntax that should be included in all graph syntax are highlighted in **bold**:

| Statistical Package | Syntax Example |
|--------------------|----------------|
| R                  | `library(foreign)`<br>`library(readstata13)`<br>`data <- read.LIS("lu10p")`<br>`attach(data)`<br>**`png(file = paste0(USR_PDF,”/graphtestR.png”),width=1200,height=1000)`**<br>`plot(edyrs, pi11)`<br>`abline(lm(pi11~edyrs))`<br>`title(“Regression of education on wage”)` |
| SAS                | **`FILENAME output “&mypdf/graphtestsas.png”;`**<br>**`GOPTIONS RESET=ALL DEVICE=PNG GSFNAME=output GSFMODE=REPLACE;`**<br>`PROC GCHART data=&lu10p;`<br>`VBAR age / TYPE=percent;`<br>`RUN;` |
| SPSS               | `GET FILE = lu10p`<br>`GRAPH`<br>`/BAR(SIMPLE)=relation BY edyrs.`<br>**`OUTPUT EXPORT /JPG DOCUMENTFILE=”mypdf\graphtestspss.jpg`** |
| Stata              | `use $lu10p, clear`<br>`twoway (lfit pi11 edyrs)`<br>**`graphexportpdf $mypdf/graphteststata`** |

## List of LIS and LWS Datasets

[LIS](https://www.lisdatacenter.org/) supplies a file that includes a list of datasets that can be used through [LISSY](https://www.lisdatacenter.org/data-access/lissy/), including characteristics to identify [LIS](https://www.lisdatacenter.org/) and [LWS](https://www.lisdatacenter.org/data-access/lws/) online datasets.

The file exists in either `.dta` or `.txt` format. See below the syntax to access these files in [R](https://www.r-project.org/), [SAS](https://www.sas.com/), or [Stata](https://www.stata.com/). You can also download the file from [here](https://www.lisdatacenter.org/data-access/lissy/).

| Database | File | Statistical Package | Syntax |
|----------|------|--------------------|--------|
| LIS / LWS | List of datasets | R | `read.dta13(paste(INC_DIR, "datasets.dta", sep=""),convert.factors=FALSE)` |
|           |                  | SAS | `PROC IMPORT DATAFILE=”&myincl.datasets.txt” OUT= datasets replace DBMS=dlm; delimiter=','; RUN;` |
|           |                  | Stata | `use $myincl/datasets.dta` |

## LIS PPPs Deflators

[LIS](https://www.lisdatacenter.org/) provides a list of [LIS PPPs deflators](https://www.lisdatacenter.org/data-access/lissy/) that can be accessed through [LISSY](https://www.lisdatacenter.org/data-access/lissy/).

The list of [LIS PPPs deflators](https://www.lisdatacenter.org/data-access/lissy/) enables adjusting either income, consumption, or wealth variables in a given country in a given year to 2011 or 2017 USD PPPs (files `ppp_2017` and `ppp_2011`). This list is also available online [here](https://www.lisdatacenter.org/data-access/lissy/).

Each file exists in either `.dta` or `.txt` format. See below the syntax to access these files in [R](https://www.r-project.org/), [SAS](https://www.sas.com/), or [Stata](https://www.stata.com/):

| Database | File | Statistical Package | Syntax |
|----------|------|--------------------|--------|
| LIS / LWS | List of datasets | R | `read.dta13(paste(INC_DIR, "ppp_2017.dta", sep=""),convert.factors=FALSE)` |
|           |                  | SAS | `PROC IMPORT DATAFILE=”&myincl.ppp_2017.txt” OUT=ppps replace DBMS=dlm; delimiter=','; RUN;` |
|           |                  | Stata | `use $myincl/ppp_2017.dta` |

Note: The old [LIS 2011 PPPs](https://www.lisdatacenter.org/data-access/lissy/) file is still accessible via [LISSY](https://www.lisdatacenter.org/data-access/lissy/).

## Data Archiving System in LISSY

(Applies only to datasets that underwent revision after May/June 2019 and for journal review purposes only).

Following the 2019 [LIS Template](https://www.lisdatacenter.org/) release in May/June 2019, [LIS](https://www.lisdatacenter.org/) introduced a new data archiving system. To continue adding new datasets and new countries while maintaining cross-country comparability and high-quality data, revisions to existing datasets are occasionally carried out. The data archiving system tool allows replicating the analysis on datasets uploaded in [LISSY](https://www.lisdatacenter.org/data-access/lissy/) after May/June 2019 and subsequently revised. This tool is only for peer review activities or researchers who need to replicate published results. Access is granted for a maximum period of two weeks.

### How to Request Access to an Earlier Version of Revised Datasets?

To replicate analysis carried out on a pre-revised dataset, contact [LIS user support](mailto:usersupport@lisdatacenter.org) at [usersupport@lisdatacenter.org](mailto:usersupport@lisdatacenter.org), specifying the following:

- The Database ([LIS](https://www.lisdatacenter.org/)/[LWS](https://www.lisdatacenter.org/data-access/lws/)).
- The Statistical package ([Stata](https://www.stata.com/), [R](https://www.r-project.org/), [SAS](https://www.sas.com/), [SPSS](https://www.ibm.com/products/spss-statistics)).
- Date of accessing the dataset(s) and running the analysis.

You will subsequently receive an email with instructions on how to access the pre-revised datasets.

For users interested in accessing the Databases following the 2011 Template (i.e., the last version of the datasets on [LISSY](https://www.lisdatacenter.org/data-access/lissy/) prior to May 2019 for [LIS](https://www.lisdatacenter.org/) and mid-June for [LWS](https://www.lisdatacenter.org/data-access/lws/)), choose the project “LISPRE” from [LISSY](https://www.lisdatacenter.org/data-access/lissy/) for the [LIS](https://www.lisdatacenter.org/) Database, and “LWSPRE” for the [LWS](https://www.lisdatacenter.org/data-access/lws/) Database.

## LISSY Coding Best Practices

The [LISSY](https://www.lisdatacenter.org/data-access/lissy/) system processes received jobs and returns listings with aggregated results, usually within minutes. However, [LISSY](https://www.lisdatacenter.org/data-access/lissy/)’s processing time can vary depending on the total number of submitted jobs at a given time and the complexity of each job. To avoid system congestion, we recommend the following:

- Send each job only once. If it is not returned, do not send it again.
- Wait for each job to be returned before submitting your next one.
- Do not request frequencies on continuous variables, as this violates our security measures.
- Do not attempt to view, examine, or print individual records at either the person or household level. Violating this rule could result in the termination of your [LISSY](https://www.lisdatacenter.org/data-access/lissy/) access.
- Do not use commands that violate our security measures. Certain program syntax and commands will trigger system security alerts and may interrupt traffic. See our [FAQs](https://www.lisdatacenter.org/data-access/lissy/) for tips on avoiding disallowed commands under the question “What does set for review mean, and how can I avoid this?”.
- Try breaking up statistical queries into several smaller jobs, as jobs that result in very long output may cause system congestion. If you encounter difficulties repeatedly, please contact [User Support](mailto:usersupport@lisdatacenter.org).
- Debug your program before submitting a job to [LISSY](https://www.lisdatacenter.org/data-access/lissy/), especially if you are not familiar with statistical package syntax. Debugging can be done on your home computer by testing your jobs on our downloadable [sample files](https://www.lisdatacenter.org/data-access/lissy/).

# Managing LISSY Jobs and Listings – FAQs

## What statistical packages can I use with LISSY?

[R](https://www.r-project.org/) (4.0.5), [SAS](https://www.sas.com/) (9.4), [SPSS](https://www.ibm.com/products/spss-statistics) (22), and [Stata](https://www.stata.com/) (16.1) programs all work with [LISSY](https://www.lisdatacenter.org/data-access/lissy/).

## May I use external files with the LIS databases?

If you wish to use external files with the microdata, send your request, along with the attached file, to [usersupport@lisdatacenter.org](mailto:usersupport@lisdatacenter.org). Your request will be reviewed, and if it meets our security standards, you will receive an email with instructions on how to access your file.

## What does "set for review" mean, and how can I avoid this?

[LISSY](https://www.lisdatacenter.org/data-access/lissy/) automatically applies pre- and post-processing checks on received jobs and produced listings to authenticate the user and ensure that the confidentiality of our data is never breached. Some program syntaxes and commands may trigger security alerts, such as syntax that displays frequencies on continuous variables or that would allow users to print individual records. When [LISSY](https://www.lisdatacenter.org/data-access/lissy/) detects a potentially suspicious job, it stores it in a security area for manual review and sends the error message "set for review."

To avoid this:

- Adjust your code to avoid syntax that could potentially print variables, regardless of the programming language used.
- Do not include the following commands in your job:

| Statistical Package | Disallowed Commands |
|--------------------|---------------------|
| SAS                | `print`, `NOXWAIT`, `NOXSYNC` |
| SPSS               | `print` |
| Stata              | `list`, `erase`, `rm`, `pwd`, `cd`, `rmdir`, `type`, `dir`, `ls` |

Jobs set for review are manually checked, which may take some time. In the meantime, avoid resending the same job until it has been processed.

## What does “handling listing” or “job has been automatically killed” mean, and how can I avoid this?

The most common reason [LISSY](https://www.lisdatacenter.org/data-access/lissy/) holds listings in the secure area for review is that listings are excessively long. To avoid this:

- Split your program code into smaller parts and send several shorter job submissions.
- Limit the number of datasets combined in a single run as much as possible.
- Include statistical commands to shorten outputs, such as:

| Statistical Package | Commands to Shorten Output |
|--------------------|---------------------------|
| SAS                | `OPTIONS nosource nonotes` |
| Stata              | `nolog`, `quietly`, or `noisily` |

## I get an error message in my output. Is there a way to debug my program?

Debugging can be facilitated by testing your code on [LIS](https://www.lisdatacenter.org/) or [LWS](https://www.lisdatacenter.org/data-access/lws/) downloadable [sample files](https://www.lisdatacenter.org/data-access/lissy/) on your own computer before submitting to [LISSY](https://www.lisdatacenter.org/data-access/lissy/). Be aware that these artificial samples, which include a small sub-sample of randomly selected households and their respective household members, are created for instructional and debugging purposes only and cannot be used to draw conclusions.

## Can I receive non-ASCII output/listings from LISSY such as worksheets, HTML pages, etc.?

Currently, [LISSY](https://www.lisdatacenter.org/data-access/lissy/) only sends back plain ASCII output/listings from [SAS](https://www.sas.com/), [SPSS](https://www.ibm.com/products/spss-statistics), [R](https://www.r-project.org/), and [Stata](https://www.stata.com/).

## Why do I receive the error message "Could not connect to the server"?

The [Job Submission Interface](https://www.lisdatacenter.org/data-access/lissy/) may freeze, or an error message "Could not connect to the server" may be sent when [LISSY](https://www.lisdatacenter.org/data-access/lissy/) is temporarily down. Contact [user support](mailto:usersupport@lisdatacenter.org) at [usersupport@lisdatacenter.org](mailto:usersupport@lisdatacenter.org) if you encounter this issue.

## I get the error message "wrong header." How can I avoid this?

This error message is received when submitting a job via email and [LISSY](https://www.lisdatacenter.org/data-access/lissy/) cannot properly read the first four-line header of the job. The easiest and recommended way to solve this problem is to submit jobs via the web-based [Job Submission Interface](https://www.lisdatacenter.org/data-access/lissy/).

If you prefer to submit jobs via email, ensure the following requirements are met for [LISSY](https://www.lisdatacenter.org/data-access/lissy/) to process jobs properly, regardless of the programming language used:

- All emails must be sent in ASCII/plain text format. Ensure your email software is properly configured.
- All job instructions must be written inside the body of the email and not as an attachment.
- Each job must start exactly with a specific four-line header at the very beginning of the email body:

```
*user = <your userid>
*password = <your password> (case-sensitive)
*package = <statistical package chosen> (SAS, SPSS, Stata or R)
*project = <project to access> (LIS or LWS)
```

If the header contains an error, [LISSY](https://www.lisdatacenter.org/data-access/lissy/) returns an error message email to the address from which the job request was submitted.

## Additional Support

If you experience a specific issue not addressed above, contact [usersupport@lisdatacenter.org](mailto:usersupport@lisdatacenter.org). When related to [LISSY](https://www.lisdatacenter.org/data-access/lissy/), provide the following information whenever possible:

1. The type of access used (web-based [Job Submission Interface](https://www.lisdatacenter.org/data-access/lissy/) versus email).
2. The network and operating system from which you attempted to access [LISSY](https://www.lisdatacenter.org/data-access/lissy/) (e.g., at Princeton University on Windows 7 64-bit).
3. A description of the exact stage at which the issue occurs. Any screenshot is welcome.
4. The error message you received, if any.
5. The date and time when the problem occurred.
6. If the problem is related to a specific job, mention the job number.

# LISSY Coding Best Practices

The [LISSY](https://www.lisdatacenter.org/data-access/lissy/) system processes received jobs and returns listings with aggregated results, typically within minutes. However, processing time may vary depending on the total number of submitted jobs and the complexity of each job. To avoid system congestion, adhere to the following recommendations:

- Submit each job only once. If it is not returned, refrain from resending it.
- Wait for each job to be returned before submitting the next one.
- Avoid requesting frequencies on continuous variables, as this violates [LISSY](https://www.lisdatacenter.org/data-access/lissy/) security measures.
- Do not attempt to view, examine, or print individual records at the person or household level. Violating this rule may result in the termination of your [LISSY](https://www.lisdatacenter.org/data-access/lissy/) access.
- Refrain from using commands that violate security measures. Certain program syntax and commands may trigger system security alerts and interrupt traffic. Refer to the [FAQs](https://www.lisdatacenter.org/data-access/lissy/managing-lissy-jobs-and-listings-faqs/) for tips on avoiding disallowed commands under the question “What does set for review mean, and how can I avoid this?”.
- Break up statistical queries into several smaller jobs, as jobs producing very long outputs may cause system congestion. If difficulties persist, contact [User Support](mailto:usersupport@lisdatacenter.org).
- Debug your program before submitting it to [LISSY](https://www.lisdatacenter.org/data-access/lissy/), especially if you are unfamiliar with statistical package syntax. Debugging can be performed on your personal computer using [LISSY’s downloadable sample files](https://www.lisdatacenter.org/data-access/lissy/).

# LIS Database

The [Luxembourg Income Study Database (LIS)](https://www.lisdatacenter.org/) is the largest available income database of harmonized microdata, covering 52 countries across Europe, North America, Latin America, Africa, Asia, and Australasia, spanning five decades.

Harmonized into a common framework ([2024 Template LIS User Guide](https://www.lisdatacenter.org/our-data/lis-database/)), [LIS](https://www.lisdatacenter.org/) datasets contain household- and person-level data ([List of Variables](https://www.lisdatacenter.org/our-data/lis-database/), [Printable version](https://www.lisdatacenter.org/our-data/lis-database/)) on labor income, capital income, pensions, public social benefits (excluding pensions), private transfers, taxes and contributions, demography, employment, and expenditures.

## Content of LIS Flow Variables

To provide detailed documentation, [LIS](https://www.lisdatacenter.org/) has published comprehensive content tables for the flow variables of each dataset, available in two downloadable Excel documents. The information is organized by country and, within each country, by year, offering users a thorough overview.

- [How to read the tables](https://www.lisdatacenter.org/our-data/lis-database/)
- [Flow Variables](https://www.lisdatacenter.org/our-data/lis-database/): Detailed information on the content of [LIS](https://www.lisdatacenter.org/) flow variables.
- [Public Transfers by type (alternative set)](https://www.lisdatacenter.org/our-data/lis-database/): Detailed information on the content of [LIS](https://www.lisdatacenter.org/) variables for the alternative set of public transfers by type.

Note: These documents are updated each time [LIS](https://www.lisdatacenter.org/) releases new datasets, including new countries, additional years for existing countries, and any revisions to previous data.

## Generic Codebook and Extensive Documentation

- For a generic codebook of [LIS Database](https://www.lisdatacenter.org/) variables’ names, definitions, codes, and comments, see [here](https://www.lisdatacenter.org/our-data/lis-database/).
- For extensive documentation on the [LIS Database](https://www.lisdatacenter.org/), access [METIS](https://www.lisdatacenter.org/our-data/metis/).

## List of LIS Datasets

Note: The year given is the income reference year, corresponding to the year to which the income data pertain.

Newly added datasets ([2025 Autumn Data Splash](https://www.lisdatacenter.org/our-data/lis-database/)) are listed in blue.  
Forthcoming datasets are listed in red.

| Country           | Historical Data | Wave I (~1980)       | Wave II (~1985)    | Wave III (~1990)   | Wave IV (~1995)    | Wave V (~2000)     | Wave VI (~2004)    | Wave VII (~2007)   | Wave VIII (~2010)  | Wave IX (~2013)   | Wave X (~2016)    | Wave XI (~2019)   | Wave XII (~2022)  | Wave XIII (~2025) |
|-------------------|-----------------|----------------------|---------------------|---------------------|---------------------|---------------------|---------------------|---------------------|---------------------|-------------------|-------------------|-------------------|-------------------|-------------------|
| Australia         |                 | AU81                 | AU85                | AU89                | AU95                | AU01                | AU03 AU04           | AU08                | AU10                | AU14              | AU16              | AU18 AU20         |                   |                   |
| Austria           |                 |                      |                     |                     | AT94 AT95 AT96 AT97 | AT98 AT99 AT00      | AT03 AT04 AT05      | AT06 AT07 AT08      | AT09 AT10 AT11     | AT12 AT13 AT14    | AT15 AT16 AT17    | AT18 AT19 AT20    | AT21 AT22         |                   |
| Belgium           |                 |                      | BE85                | BE88 BE92           | BE95 BE97           | BE00                | BE03 BE04 BE05      | BE06 BE07 BE08      | BE09 BE10 BE11     | BE12 BE13 BE14    | BE15 BE16 BE17    | BE18 BE19 BE20    | BE21              |                   |
| Brazil            |                 | BR81 BR82            | BR83 BR84 BR85 BR86 BR87 | BR88 BR89 BR90 BR92 | BR93 BR95 BR96 BR97 | BR98 BR99 BR01 BR02 | BR03 BR04 BR05      | BR06 BR07 BR08      | BR09 BR11          | BR12 BR13 BR14    | BR15 BR16 BR17    | BR18 BR19 BR20    | BR21 BR22         |                   |
| Bulgaria          |                 |                      |                     |                     |                     |                     |                     | BG07 BG08           | BG09 BG10 BG11      | BG12 BG13 BG14    | BG15 BG16 BG17    | BG18 BG19 BG20    | BG21 BG22         |                   |
| Canada            | CA71 CA73 CA75 | CA77 CA79 CA81 CA82 | CA84 CA85 CA86 CA87 | CA88 CA89 CA90 CA91 CA92 | CA93 CA94 CA95 CA96 CA97 | CA98 CA99 CA00 CA01 CA02 | CA03 CA04 CA05 | CA06 CA07 CA08 | CA09 CA10 CA11 | CA12 CA13 CA14 | CA15 CA16 CA17 | CA18 CA19 CA20 | CA21              |                   |
| Chile             |                 |                      |                     | CL90 CL92           | CL94 CL96           | CL98 CL00           | CL03                | CL06                | CL09 CL11          | CL13              | CL15 CL17         |                   |                   |                   |
| China             |                 |                      |                     |                     |                     | CN02                |                     |                     |                     | CN13              |                   | CN18              |                   |                   |
| Colombia          |                 |                      |                     |                     |                     | CO01 CO02           | CO03 CO04 CO05      | CO06 CO07 CO08      | CO09 CO10 CO11     | CO12 CO13 CO14    | CO15 CO16 CO17    | CO18 CO19 CO20    | CO21 CO22 CO23    |                   |
| Czechia           |                 |                      |                     | CZ92                | CZ96                | CZ02                | CZ04 *CZ05          | *CZ06 CZ07 *CZ08    | *CZ09 CZ10 *CZ11   | *CZ12 CZ13 *CZ14  | *CZ15 CZ16 *CZ17  | *CZ18 *CZ19 *CZ20 | *CZ21 *CZ22 *CZ23 |                   |
| Denmark           |                 |                      | DK87                | DK92                | DK95                | DK00                | DK04                | DK07                | DK10               | DK13              | DK15 DK16 DK17    | DK18 DK19 DK20    | DK21 DK22         |                   |
| Dominican Rep.    |                 |                      |                     |                     |                     |                     |                     | DO07                |                     |                   |                   |                   |                   |                   |
| Estonia           |                 |                      |                     |                     |                     | EE00                | EE04                | EE07                | EE10               | EE13              | EE16              |                   |                   |                   |
| Finland           |                 |                      | FI87                | FI91                | FI95                | FI00                | FI04                | FI07                | FI10               | FI13              | FI16              |                   |                   |                   |
| France            | FR70 FR75      | FR79                 | FR84                | FR90                | FR96 FR97           | FR98 FR99 FR00 FR01 FR02 | FR03 FR04 FR05 | FR06 FR07 FR08 | FR09 FR10 FR11 | FR12 FR13 FR14 | FR15 FR16 FR17 | FR18 FR19 FR20 | FR21              |                   |
| **Mali**          |                 |                      |                     |                     |                     |                     |                     |                     | ML11               | ML13 ML14         | ML15 ML16 ML17    | ML18 ML19 ML20    |                   |                   |
| Mexico            |                 |                      | MX84                | MX89 MX92           | MX94 MX96           | MX98 MX00 MX02      | MX04 MX05           | MX06 MX08           | MX10               | MX12 MX14         | MX16              | MX18 MX20         | MX22              |                   |
| Netherlands       |                 |                      | NL83 NL87           | NL90                | NL93                | NL99                | NL04 NL05           | NL06 NL07 NL08      | NL09 NL10 NL11     | NL12 NL13 NL14    | NL15 NL16 NL17    | NL18 NL19 NL20    | NL21              |                   |
| Norway            |                 | NO79                 | NO86                | NO91                | NO95                | NO00                | NO04                | NO07                | NO10               | NO13              | NO16              | NO19 NO20         | NO21 NO22         |                   |
| Palestine         |                 |                      |                     |                     |                     |                     |                     |                     |                     |                   | PS17              |                   | PS23              |                   |
| Panama            |                 |                      |                     |                     | *PA96 *PA97        | *PA98 *PA99 *PA00 *PA01 *PA02 | *PA03 *PA04 *PA05 | *PA06 PA07 *PA08 | *PA09 PA10 *PA11 | *PA12 PA13 *PA14 | *PA15 PA16 *PA17 | *PA18 *PA19 *PA20 | *PA21 *PA22       |                   |
| Paraguay          |                 |                      |                     |                     | PY97                | PY99 PY00 PY02      | PY03 PY04 PY05      | PY06 PY07 PY08      | PY09 PY10 PY11     | PY12 PY13 PY14    | PY15 PY16 PY17    | PY18 PY19 PY20    | *PY21 *PY22       |                   |
| Peru              |                 |                      |                     |                     |                     |                     | PE04 PE05           | PE06 PE07 PE08      | PE09 PE10 PE11     | PE12 PE13 PE14    | PE15 PE16 PE17    | PE18 PE19 *PE20   | PE21              |                   |
| Poland            |                 |                      | PL86                | PL92                | PL95                | PL99                | PL04 PL05           | PL06 PL07 PL08      | PL09 PL10 PL11     | PL12 PL13 PL14    | PL15 PL16 PL17    | PL18 PL19 PL20    | PL21 PL22 PL23    |                   |
| Romania           |                 |                      |                     |                     | RO95 RO97           |                     |                     | RO06 RO07 RO08      | RO09 RO10 RO11     | RO12 RO13 RO14    | RO15 RO16 RO17    | RO18 RO19 RO20    | RO21              |                   |
| Russia            |                 |                      |                     |                     |                     | RU00                | RU04                | RU07                | RU10 RU11          | RU13 RU14         | RU15 RU16 RU17    | RU18 RU19 RU20    | RU21 RU22         |                   |
| Serbia            |                 |                      |                     |                     |                     |                     |                     | RS06 RS07 RS08      | RS09 RS10 RS11     | RS12 RS13 RS14    | RS15 RS16 RS17    | RS18 RS19         | RS21 RS22         |                   |
| Slovakia          |                 |                      |                     | SK92                | SK96                |                     | SK04                | SK07                | SK10               | SK13 SK14         | SK15 SK16 SK17    | SK18              |                   |                   |
| Slovenia          |                 |                      |                     |                     | SI97                | SI99                | SI04                | SI07                | SI10               | SI12              | SI15              |                   |                   |                   |
| South Africa      |                 |                      |                     |                     |                     |                     |                     | ZA08                | ZA10               | ZA12              | ZA15 ZA17         |                   |                   |                   |
| South Korea       |                 |                      |                     |                     |                     |                     | KR06                | KR08                | KR10               | KR12 KR14         | KR16 KR17         | KR18 KR19 KR20    | KR21              |                   |
| Spain             |                 | ES80                 | ES85                | ES90                | ES93 ES94 ES95 ES96 ES97 | ES98 ES99 ES00 | ES04 ES05 | ES06 ES07 ES08 | ES09 ES10 ES11 | ES12 ES13 ES14 | ES15 ES16 ES17 | ES18 ES19 ES20 | ES21 ES22       |                   |
| Sweden            | SE75            | SE81                 | SE87                | SE92                | SE95                | SE00 SE01 SE02      | SE03 SE04 SE05      | SE06 SE07 SE08      | SE09 SE10 SE11     | SE12 SE13 SE14    | SE15 SE16 SE17    | SE18 SE19 SE20    | SE21              |                   |
| Switzerland       |                 | CH82                 |                     | CH92                |                     | CH00 CH02           | CH04                | CH06 CH07 CH08      | CH09 CH10 CH11     | CH12 CH13 CH14    | CH15 CH16 CH17    | CH18 CH19 CH20    | CH21 CH22         |                   |
| Taiwan            |                 | TW81                 | TW86                | TW91                | TW95 TW97           | TW00                | TW05                | TW07                | TW10               | TW13              | TW16 TW17         | TW18 TW19 TW20    | TW21              |                   |
| United Kingdom    | UK68 UK69 UK70 UK71 UK72 UK73 UK74 UK75 UK76 UK77 | UK78 UK79 UK80 UK81 UK82 | UK83 UK84 UK85 UK86 UK87 | UK88 UK89 UK90 UK91 UK92 | UK93 UK94 UK95 UK96 UK97 | UK98 UK99 UK00 UK01 UK02 | UK03 UK04 UK05 | UK06 UK07 UK08 | UK09 UK10 UK11 | UK12 UK13 UK14 | UK15 UK16 UK17 | UK18 UK19 UK20 | UK21            |                   |
| United States     | US63 US64 US65 US66 US67 US68 US69 US70 US71 US72 US73 US74 US75 US76 US77 | US78 US79 US80 US81 US82 | US83 US84 US85 US86 US87 | US88 US89 US90 US91 US92 | US93 US94 US95 US96 US97 | US98 US99 US00 US01 US02 | US03 US04 US05 | US06 US07 US08 | US09 US10 US11 | US12 US13 US14 | US15 US16 US17 | US18 US19 US20 | US21 US22 US23 |                   |
| Uruguay           |                 |                      |                     |                     |                     |                     | UY04 UY05           | UY06 UY07 UY08      | UY09 UY10 UY11     | UY12 UY13 UY14    | UY15 UY16 UY17    | UY18 UY19         | UY22 UY23         | UY24              |
| **Vietnam**       |                 |                      |                     |                     |                     |                     |                     | VN05 VN07           | VN09 VN11          | VN13              |                   |                   |                   |                   |

**The inclusion of Ivory Coast, Mali, and Vietnam was accomplished through research agreements between the [Agence Française de Développement (AFD)](https://www.afd.fr/) and [LIS](https://www.lisdatacenter.org/). [LIS](https://www.lisdatacenter.org/) is grateful for this cooperation, which enabled these valuable additions.

For convenience, [LIS](https://www.lisdatacenter.org/) uses short country/territory names—those commonly used in cross-national academia—in conjunction with standard two-letter [ISO abbreviations](https://www.iso.org/iso-3166-country-codes.html). This convention does not imply any opinion on the part of [LIS](https://www.lisdatacenter.org/) concerning the legal status of any country or territory. [LIS](https://www.lisdatacenter.org/) acknowledges that several supranational organizations may designate country/territory names that differ from those used by [LIS](https://www.lisdatacenter.org/), including:

- [United Nations](https://www.un.org/)
- [World Bank](https://www.worldbank.org/)
- [International Labour Organization](https://www.ilo.org/)
- [Organisation for Economic Co-operation and Development](https://www.oecd.org/)

# Compare.It — LIS Comparability Tool

[Compare.It](https://comparability.lisdatacenter.org/shiny/comparability/), the new Comparability Tool from [LIS](https://www.lisdatacenter.org/), aims to inform users about country-specific data comparability issues in a concise manner. The tool is an innovative addition to the [LIS METadata Information System (METIS)](https://www.lisdatacenter.org/our-data/metis/).

[Access Compare.It](https://comparability.lisdatacenter.org/shiny/comparability/)

Please note that [Compare.It](https://comparability.lisdatacenter.org/shiny/comparability/) is not intended for cross-country comparisons. For visualizing income and wealth indicators across countries and over time, users are advised to use [DART](https://www.lisdatacenter.org/data-access/dart/).


## Compare.It Main Features

- Displays the survey series harmonized in a country for the [Luxembourg Income Study (LIS) Database](https://www.lisdatacenter.org/) and the [Luxembourg Wealth Study (LWS) Database](https://www.lisdatacenter.org/data-access/lws/).
- Documents methodological changes within a country’s survey series and major deviations from [LIS](https://www.lisdatacenter.org/) general harmonization practices.
- Presents new country-level indicators: 1) coverage ratios of [LIS](https://www.lisdatacenter.org/) datasets versus [National Accounts](https://www.oecd.org/), and 2) inequality estimates with confidence intervals.
- Enables users to access: 
  1. Information about country-level consistency and limitations of [LIS](https://www.lisdatacenter.org/) harmonization efforts.
  2. Visualization of inequality measures by the underlying country series.
  3. Continuously updated comparisons between aggregated microdata and [National Accounts](https://www.oecd.org/) figures.

Currently, the tool covers a subset of [LIS](https://www.lisdatacenter.org/) countries, with more countries to be gradually added.

## What is this app for?

This tool is designed to highlight issues related to the consistency and comparability of data series in the [LIS](https://www.lisdatacenter.org/) and [LWS](https://www.lisdatacenter.org/data-access/lws/) databases. It displays the survey series available in a country and identifies instances where methodological changes occurred within those series. Researchers should note breaks in series caused by switching surveys or interruptions within ongoing surveys.

## How can I compare different countries?

This tool is not intended for cross-country comparisons. For visualizing trends of indicators across countries, use the [LIS DART tool](https://www.lisdatacenter.org/data-access/dart/).
