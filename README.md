## Overview
> The goal of this project is to build a chrome extension that can provide credibility and readability scores of a news article. <br/>
> Readability scores are generated from formula proposed by Flesch and Kincaid (F-K).<br/>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;See: https://en.wikipedia.org/wiki/Flesch–Kincaid_readability_tests<br/>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Specifically, they are F-K score and F-K grade level<br/>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source code: https://github.com/cdimascio/py-readability-metrics<br/>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Input: a string that contains the content to be assessed<br/>

## Modules Provided
> manifest.json is a required file in chrome extension.
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Future versions can:
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1. Add functionality of automatically popping up when the user visits an article
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2. Add functionality of getting the url of the article for automated computation of scores
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3. Design and add icons for better aesthetics
> learning.html is the popup window that makes up the chrome extension.
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Future versions can:
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1. Add .js javascripts to automate computation of scores (Need to bridge language gap between Python and Javascript modules)
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2. Improve aesthetics
> 
### Current 
