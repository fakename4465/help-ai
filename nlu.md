version: "3.1"

nlu:
- intent: greet
  examples: |
    - hey
    - hello
    - hi
    - good morning
    - good evening
    - hey there
    - heya
    - yo

- intent: goodbye
  examples: |
    - bye
    - goodbye
    - see you around
    - see you later
    - cya
    - talk to you later

- intent: affirm
  examples: |
    - yes
    - indeed
    - of course
    - that sounds good
    - correct
    - yup
    - sure

- intent: deny
  examples: |
    - no
    - never
    - I don't think so
    - not really
    - nope
    - nah

- intent: bot_challenge
  examples: |
    - are you a bot?
    - are you human?
    - am I talking to a bot?
    - am I talking to a human?

- intent: schedule_meeting
  examples: |
    - book a meeting for [tomorrow](date)
    - schedule a meeting with [John](attendees)
    - set up a meeting for [Friday](date) at [3pm](time)
    - can you schedule a meeting?
    - I want to set up a call for [next Monday at 10am](time)
    - arrange a meeting with [Sarah](attendees) and [Mike](attendees) for [Wednesday](date)
    - book a meeting room in [New York office](location)
    - schedule a meeting about the project status [tomorrow morning](time) in [conference room A](location)
    - Need to book a meeting for [next Tuesday](date)
    - Let's schedule a meeting [tomorrow](date) at [2 PM](time) with [Alice](attendees) and [Bob](attendees) in the [main conference room](location)
    - I'd like to schedule something for [Friday afternoon](time)
    - Please find a slot for a meeting with [the team](attendees) on [the 25th of this month](date)

- intent: reset_password
  examples: |
    - I need to reset my password
    - reset my password please
    - password reset
    - I've forgotten my password
    - help me with password
    - Can you reset my password for employee ID [12345](employee_id)?
    - My password isn't working
    - Need help resetting my password, my ID is [E7890](employee_id)

- intent: inform # Generic intent for providing information, especially for forms
  examples: |
    - it's for [tomorrow](date)
    - [3pm](time)
    - [John](attendees)
    - [conference room B](location)
    - [12345](employee_id)
    - my employee ID is [E7890](employee_id)
    - [next week](date)
    - [Sarah Jones](attendees) and [Peter Pan](attendees)
    - [London office](location)
    - [10 AM](time)
    - The date is [August 15th](date)
    - Time should be [around 4 PM](time)
    - Invite [Mary](attendees), [David](attendees), and [Susan](attendees)
    - The location is [online](location)
    - My employee id is [EMP007](employee_id)

- intent: out_of_scope
  examples: |
    - what's the weather like?
    - tell me a joke
    - who are you?
    - what is your name?
    - what can you do?
    - how does this work?
    - can you order pizza?