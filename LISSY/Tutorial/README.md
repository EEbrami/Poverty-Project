# LISSY

## What is LISSY?

LISSY is a remote-execution system that allows researchers to access [LIS](https://www.lisdatacenter.org/) and [LWS](https://www.lisdatacenter.org/data-access/lws/) microdata from a remote location while adhering to the privacy restrictions mandated by the countries providing the data. It offers secure access to the microdata through a web-based [Job Submission Interface](https://www.lisdatacenter.org/data-access/lissy/).

## How to Register for LISSY?

[LIS](https://www.lisdatacenter.org/) grants access to its micro-databases to registered users for a period of one year, renewable annually.

[Register for access to LISSY](https://www.lisdatacenter.org/data-access/lissy/)

## How to Get Started with LISSY?

Users write and submit statistical programs written in [R](https://www.r-project.org/), [SAS](https://www.sas.com/), [SPSS](https://www.ibm.com/products/spss-statistics), or [Stata](https://www.stata.com/) through the [LISSY interface](https://www.lisdatacenter.org/data-access/lissy/) (Batch coding mode). LISSY automatically processes the jobs and typically returns aggregated results to users within a few minutes.

To ensure proper processing of user requests, LISSY requires a few exceptions to the standard statistical program syntax.

[View Job Submission Guide](https://www.lisdatacenter.org/data-access/lissy/)

## LIS’ Rules for Citation

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
