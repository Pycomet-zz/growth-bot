<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->

[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<!-- PROJECT LOGO -->
<br />
<p align="center">
  <!-- <a href="https://github.com/Pycomet/telegram-group-engagement-bot">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a> -->

  <h3 align="center">Telegram Growth Bot</h3>

  <p align="center">
    The primary function of this bot is to grow telegram groups to unbelievably huge number of members.
    <br />
    <a href="https://github.com/Pycomet/growth-bot"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/Pycomet/growth-bot">View Demo</a>
    ·
    <a href="https://github.com/Pycomet/growth-bot/issues">Report Bug</a>
    ·
    <a href="https://github.com/Pycomet/growth-bot/issues">Request Feature</a>
  </p>
</p>

<!-- ABOUT THE PROJECT -->

### About The Project

This is a custom built telegram bot script application to add users embedded in a User Friendly process oriented bot to handle the onbarding and smooth flow of the service provided. Which is extracting users from specified target groups and adding them into the user's own group.

### Here are the processes followed

After initiating the `/start` command;

1.  The bot requests for the group you would like to extract members from ? (it has to be a group with members and not a channel with subscribers)

2.  The bot requests for an index point to start the adding process from. This basically helps you start off from where you left off the previous day after extract from the group used in `step 1`.

NOW IS THE BOT'S TURN 🤓

1.  Th first thing the bot does is fetch all the client sessions it has access to as preconfigured. All into a list.

2.  Using each of the sessions, one at a time. The bot used the client user to add the extracted user into the target group with a maximum of 50 on each client (Maximum number of adds per day).

The index is always registered to the runtime memory, so whichever the client that is used. The application is not going over the same users twice.

... And after all is done, the bot signifies, the number of users added, the number of failed attempts and finally says bye, hoping to see you in around 24hours.

### Built With

This application is built with python entirely. With functionalities pulled from the telethon and PyTelegramBotAPI libraries.

<!-- USAGE EXAMPLES -->

### Usage

To use this application as your own, follow these simple steps;

- Fork this repository (`git clone https://github.com/Pycomet/growth-bot.git`)

- Create a `.env` file with the following data

  - `TOKEN` - This is the telegram bot token from `@botfather`
  - `GROUP` - The target telegram group you wish to grow
  - `API_ID` - Telegram api access details
  - `API_HASH` - Telegram api access details
  - `SERVER_URL` - Pre-defined web hook to be used for the app
  - `ADMIN1` - Admin telegram ID for special access

- Goto `config.py` and set `DEBUG` to "True" to run locally and "False" to run in production (With involves following the deployment process)

- Run the entrypoint file `python bot.py`

Enjoy!

## Show your support

Give a ⭐️ if this project helped you!

<!-- ROADMAP -->

### Roadmap

See the [open issues](https://github.com/Pycomet/growth-bot/issues) for a list of proposed features (and known issues).

<!-- CONTRIBUTING -->

### Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<!-- LICENSE -->

### License

Distributed under the MIT License. See `LICENSE` for more information.

<!-- CONTACT -->

### Contact

Codefred - <a href="https://www.codefred.me">www.codefred.me</a>

env -> (growthbotenv)

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[contributors-shield]: https://img.shields.io/github/contributors/Pycomet/growth-bot.svg?style=flat-square
[contributors-url]: https://github.com/Pycomet/growth-bot/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Pycomet/growth-bot.svg?style=flat-square
[forks-url]: https://github.com/Pycomet/growth-bot/network/members
[stars-shield]: https://img.shields.io/github/stars/Pycomet/growth-bot.svg?style=flat-square
[stars-url]: https://github.com/Pycomet/growth-bot/stargazers
[issues-shield]: https://img.shields.io/github/issues/Pycomet/growth-bot.svg?style=flat-square
[issues-url]: https://github.com/Pycomet/growth-bot/issues
[license-shield]: https://img.shields.io/github/license/Pycomet/growth-bot.svg?style=flat-square
[license-url]: https://github.com/Pycomet/growth-bot/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/alfredemmanuelinyang/
