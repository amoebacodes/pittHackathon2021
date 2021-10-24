## Overview
> The goal of this project is to build a chrome extension that can provide credibility and readability scores of a news article. <br/>
> Readability scores are generated from formula proposed by Flesch and Kincaid (F-K).<br/>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;See: https://en.wikipedia.org/wiki/Flesch–Kincaid_readability_tests<br/>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Specifically, they are F-K score and F-K grade level<br/>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source code: https://github.com/cdimascio/py-readability-metrics<br/>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Input: a string that contains the content to be assessed<br/>
> Credibility scores are currently generated manually, but can be automated based on a deep learning model detailed by another member in the team:<br/>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;See: https://github.com/dominicyu04/Hackthon

## Modules Provided
> manifest.json is a required file in chrome extension.<br/>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Future versions can:<br/>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1. Add functionality of automatically popping up when the user visits an article<br/>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2. Add functionality of getting the url of the article for automated computation of scores<br/>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3. Design and add icons for better aesthetics<br/>
> learning.html is the popup window that makes up the chrome extension.<br/>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Future versions can:<br/>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1. Add .js javascripts to automate computation of scores (Need to bridge language gap between Python and Javascript modules)<br/>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2. Improve aesthetics<br/>
> readabilityScore.py prints out flesch_kincaid score and grade level.<br/>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Future versions can:<br/>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1. Convert website to string. Currently done manually due to challenges of having to exclude  recommendations, ads, and other unrelated information.<br/>
