# LexTrader.io

<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name=" Rental-Market-Data-San-Fran"></a>
<img src="https://github.com/MRosan117/lex_trade_io/blob/ryan_branch/Images/banner.png">

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/github_username/repo_name">
    <img src="https://github.com/MRosan117/lex_trade_io/blob/main/Images/ml3.png" alt="Logo" width="400" height="400"> 
  </a>

<h1 align="center">LexTrader.io</h3>

  <p align="center">
    
  </p>
</div>

<!-- ABOUT THE PROJECT -->
## About The Project

<img src="https://github.com/MRosan117/lex_trade_io/blob/main/Images/giphy1.gif" alt="Logo" width="1000" height="400">
  <p align="center">
  </p>

  <p align="center" style="display: flex;" >
<img src="https://img.shields.io/npm/l/express" />
<img alt="GitHub code size in bytes" src="https://img.shields.io/github/languages/code-size/tyleradammartinez/SIG-Dashboard-Application" />
</p>

<!-- GETTING STARTED -->
## Getting Started

<br />
<div align="center">
    <img src="https://github.com/MRosan117/lex_trade_io/blob/main/Images/ml1.png" alt="Logo" width="100" height="100"> 
  </a>
  <p align="center">
  </p>
</div>

# Custom Indicator & Machine Learning Models

Our algorithmic trading uses machine learning to make predict and improve the performance of trading strategies. We use five different technical indicators, and each one is calculated on its own from real-time stock market data. After being carefully designed to pick up on different aspects of market behavior, these indicators are then put together to make a single, all-encompassing super indicator. 

These models are trained on historical and live data and use the super indicator as a key feature to predict how well our trading strategy will work overall with each indicator. This process of prediction lets us change and improve our trading strategy in real time, which increases the chances of better trading results. Overall, making the algorithmic trading more reliable and data-driven by combining traditional indicators with cutting-edge machine learning techniques.
<br />
<div align="center">
    <img src="https://github.com/MRosan117/lex_trade_io/blob/main/Images/LexTradePulse.png" alt="Logo" width="1000" height="600"> 
  
  # Alpaca
  
  <img src="https://github.com/MRosan117/lex_trade_io/blob/main/Images/alpaca.png" alt="Logo" width="1000" height="600"> 
  </a>
  <p align="center">
  </p>
</div>

# Robo Advisor with Amazon Lex
We used Amazon Lex to power an intuitive and user-friendly interface in our algorithmic trading. This interface enables us to interact with users, collect critical data, and tailor our trading strategy to their specific financial profile. When a user interacts with our system, they are asked for information such as their name, last name, date of birth, net worth, liquidity risk, level of investment experience, importance of returns, overall risk tolerance, fear index, and the amount they want to invest. We determine which portfolio category best suits the user based on their inputs, taking into account their unique preferences and risk tolerance.

This dynamic interaction ensures that each user has a personalized approach to investing that takes individual goals and comfort levels into account, allowing us to provide tailored solutions and improve the overall user experience.

<div align="center">
    <img src="https://github.com/MRosan117/lex_trade_io/blob/main/Images/lex.png" alt="Logo" width="1000" height="600"> 
  </a>
  <p align="center">
  </p>
</div>

# Monte Carlo simulation

We have incorporated Monte Carlo simulations into our algorithmic trading system to predict the performance of five different portfolios in the future. These portfolios represent a range of risk appetites, from aggressive to conservative, as indicated by different bond-to-stock ratios. We have bond-to-stock ratios of 100/0% (Conservative), 60/40% (Moderately Conservative), 40/60% (Moderate), 20/80% (Moderately Aggressive), and 0/100% (Aggressive).
Our Monte Carlo simulations generate thousands of potential future scenarios based on historical market data. This process allows us to give users a better idea of how their chosen portfolio will perform over time, taking into account market fluctuations and historical trends.This approach empowers us to make informed investment decisions that align with the users unique risk tolerance and financial objectives.

<div align="center">
    <img src="https://github.com/MRosan117/lex_trade_io/blob/main/Images/MC flow.png" alt="Logo" width="1000" height="600"> 
    <img src="https://github.com/MRosan117/lex_trade_io/blob/main/Images/MC.png" alt="Logo" width="1000" height="500"> 
  </a>
  <p align="center">
  </p>
</div>

## Required Python Libaraies

### CALCULATIONS
`pip3 install pandas` <br>
`pip3 install numpy` <br>
`pip3 install matplotlib` <br>
`pip3 install plotly` <br>
`pip3 install alpaca-py` <br>
`pip3 install alpaca-py` <br>
`pip3 install python-dotenv` <br>
`pip3 install yfinance` <br>


### APIs
* **[yfinance](https://pypi.org/project/yfinance/ "pypi yfinance Project Page")** | *Market data*
* **[Alpaca](https://alpaca.markets/")** | *Trading Platform*


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.


<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [https://github.com/othneildrew/Best-README-Template/blob/master/BLANK_README.md]()
* [https://alpaca.markets/docs/python-sdk/trading.html]()
* [https://docs.python.org/3/tutorial/controlflow.html#if-statements]()
* [https://www.simplilearn.com/tutorials/python-tutorial/python-if-else-statement#ifelse_statement]()




<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/github_username/repo_name.svg?style=for-the-badge
[contributors-url]: https://github.com/github_username/repo_name/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/github_username/repo_name.svg?style=for-the-badge
[forks-url]: https://github.com/github_username/repo_name/network/members
[stars-shield]: https://img.shields.io/github/stars/github_username/repo_name.svg?style=for-the-badge
[stars-url]: https://github.com/github_username/repo_name/stargazers
[issues-shield]: https://img.shields.io/github/issues/github_username/repo_name.svg?style=for-the-badge
[issues-url]: https://github.com/github_username/repo_name/issues
[license-shield]: https://img.shields.io/github/license/github_username/repo_name.svg?style=for-the-badge
[license-url]: https://github.com/github_username/repo_name/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/linkedin_username
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
