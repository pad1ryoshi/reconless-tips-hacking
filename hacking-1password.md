# Overview

- In this series, Ron Chan demonstrates how he went about finding multiple security vulnerabilities in 1Password.
- Just a summary of the ideas from the video series.

#  Hacking 1Password | Episode 1 - Introduction 

- How to approach web application as a Bug Bounty Hunter | Try To Understand
  - Spend a few days getting familiar with how the app works
  - Merely understanding how a application works one can uncover a lot of bugs without necessarily applying any special hacking techniques
  - Sometimes just needed to know the application threat model to spot when some of the HTTP requests were returning too much information
  - The best way to start hacking web applications is first by using them as intended
  - By understanding the intended workflows, we can create unintended workflows ourselves and if we are lucky, then we can have a security finding in the process

- Plain of the series
  - Learn the basic components of 1Password
  - Decrypt 1Password on paper
  - Decrypt 1Password together and dig deeeper
  - Put everything together
 
- Potential Areas to Test
  - View other team member's private vault
  - Guest bypass read-only permission and try to edit password items
  - Guest creates a personal vault
 
#  Hacking 1Password | Episode 2 - Decrypting the Protocol 

- Decrypting the 1Password protocol by analyzing API calls and understanding their 2x Security Derivation (2KSD)
- How 2KSD works in a high level
- MUK is computed by our email address and password
- Password items are stored and encrypted in Vault
- MUK -> Master Keysets -> Vault Keysets -> Passwords

#  Hacking 1Password | Episode 3 - Decrypting the data without Crypto Knowledge 

- Decrypting 1Password data for analysis without requiring deep cryptographic knowledge, focusing on leveraging existing online tools and resources.
  - Understanding Authentication Flow
    - Analyzing the login form with Burp Suite to monitor requests
    - Examining the Session ID, User A/User B exchange, and the MAC header for verification
    - Identifying the need to obtain the Session Key to decrypt responses 
  - Leveraging External Resources
  - Decrypting the Data 

#  Hacking 1Password | Episode 4 - Two Simple Bugs that Worth $3,300 

- Bug 1 -> Able to View Item History Even User has No Permission to Do So
  - `/vault/:vault_id/item/:item_id/history` -> 403 Forbidden returned with guest user
  - `/vault/:vault_id/item/:item_id/history/id` -> 200 OK returned with guest user
- Bug 2 -> Sensitive Info Disclosure to Lower Privileged User
  - Visit Vault page as Admin
    - API show up: `/api/v3/vault/x37...?attrs=accessors,archived-keys,activities...`
  - Make the same API request as guest user
    - Same info is returned = bug
-  Both bugs don't take a genius take to find them, a few logical thoughts and spending time to really understand the application could go a long way in bug hunting.
- Final tips
  - Start with the plan with most features on it
  - Start with the highest privileged user and later come down as a lower privileged user
  - Try to understand the target better than the people who work there




















