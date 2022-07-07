# 1. The goal of the project

The goal of the project is to develop a bot for viewing available NFT purchases, and for
view statistics for purchased NFT.
The user can add purchased NFTs (maximum 3 pieces), viewing is available
NFT for purchases, view statistics for purchased NFT, order withdrawal of funds

The term NFT refers to the NFT of a particular collection

# 2. Description of the bot

The bot consists of the following functional blocks:

1. Functional binding of NFT to the user
2. Functional view of NFTs available for purchase
3. Functional review of received NFTs
4. Functional for receiving funds
5. Functional addition of new NFTs
6. Functional language changes

## 2.1 Types of users

The bot provides three types of bot users:

- NFT owner (hereinafter Owner)
- the operator who sends the funds (hereinafter the Operator) for the first time, then it is required automate
- an admin who will be able to add new NFTs (hereinafter Admin)

## 2.2 Functional users:

Owner:

- Functional binding of NFT to the user
- Functional view of NFTs available for purchase
- Functional view of received NFTs
- Functional for receiving funds
- Functional language changes

Operator:

- Functional binding of NFT to the user
- Functional view of NFTs available for purchase
- Functional view of received NFTs
- Functional for receiving funds
- Functional language changes
- also has the ability to withhold notifications from the bot who needs to make payments

Admin:

- Functional binding of NFT to the user
- Functional view of NFTs available for purchase
- Functional view of received NFTs
- Functional for receiving funds
- Functional language changes
- Functional addition of new NFTs

## 2.3 Functional binding of NFT to the user

When purchasing an NFT on [OpenSea](https://opensea.io/), the holder will have the option
Check out the Unlockable Content which:

> Includes unlockable content only open to NFT owner.

This content will be a link with a secret code when clicked
redirects the owner to a dialogue with the bot (example link https://t.me/botnamebot?start=bdb7556d-fac3-409f-a711-4e311b50bb2f).
If the owner clicks "Start" in the bot and the bot is ready for use. For NFT to begin
all NFT machines of this type must be bought to make a profit, after they
were bought to all owners of NFT of this type receive messages that the car has been bought and
after some time start to bring profit. Maximum purchased NFTs to add to
bota should be no more than 3 pieces. If the user adds 4 NFT, then the bot meets this limit
on NFT already achieved. If the NFT was oversold, the bot responds that it was sold
and unbinds NFT from this account. It is waiting for someone to forward the link with the secret code.

## 2.4 Functional overview of NFTs available for purchase

In the bot, when the /cars command is clicked, the owner browses the available NFTs for purchases.
The view will be presented in the form of cards. The following will be displayed on the cards
information:

1. The name of the NFT
2. Collection
3. Percentage from the car
4. NFT price
5. Link to purchase on [OpenSea](https://opensea.io/)

## 2.5 Functional Review of Purchased NFTs

Clicking on the command /my owner views profitable NFTs.
The view will be presented in the form of cards. The following will be displayed on the cards
information:

1. The name of the NFT
2. Collection
3. Percentage from the car
4. NFT price

There will be a button on the card, when you click on it, you can see the statistics for this NFT

## 2.6 Functionality for receiving funds

By clicking the /request command, the owner can request the funds that have been earned by the NFT.
The command can be used once a week. Funds will be sent within 24 hours

by the operator to the owner's wallet address (this address is taken from [OpenSea](https://opensea.io/)
). If the owner has not clicked on the command / price request will be sent automatically
once a month by the operator. When requesting funds, the operator records from the bot that
you need to send funds, in the future the funds will be sent automatically.

## 2.7 Functional addition of new NFTs

With the /add bot command, ask to give a link to buy NFT (the link is generated at
[OpenSea](https://opensea.io/) when creating an NFT) then the bot generates a link with a secret
code (hereinafter Secret link) and ski gives it to the user. Then the user has to paste
it's a link in the "Unlockable Content" field so the owner can link it to theirs
account in the bot.

After the user has added the link, he has to click on the button and confirm that
he added a secret link to the NFT.

## 2.8 Functional language changes

In the /language command, the bot sends a message with three buttons to select a language.
Available languages:

- English
- Italian

When you click on the button, the bot changes the language to the selected one.

# 3. Technology stack

The following stack is offered to implement the bot:

- Python language
- PostgreSQL database
- SQLAlchemy ORM
- aiogram
- Redis NoSQL
