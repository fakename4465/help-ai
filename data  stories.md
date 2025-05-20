version: "3.1"

stories:
- story: Happy path for meeting scheduling (user provides info step-by-step)
  steps:
  - intent: greet
  - action: utter_greet
  - intent: schedule_meeting
  - action: schedule_meeting_form # Activate the form
  - active_loop: schedule_meeting_form # Form is now active
  - slot_was_set:
    - requested_slot: date # Form asks for date
  - intent: inform
    entities:
    - date: "tomorrow"
  - slot_was_set:
    - date: "tomorrow"
  - action: schedule_meeting_form # Form continues
  - slot_was_set:
    - requested_slot: time # Form asks for time
  - intent: inform
    entities:
    - time: "3pm"
  - slot_was_set:
    - time: "3pm"
  - action: schedule_meeting_form # Form continues
  - slot_was_set:
    - requested_slot: attendees # Form asks for attendees
  - intent: inform
    entities:
    - attendees: "John"
  - slot_was_set:
    - attendees: ["John"] # Note: attendees should be a list
  - action: schedule_meeting_form # Form continues
  - active_loop: null # Form is filled and deactivates
  - slot_was_set:
    - requested_slot: null
  - action: utter_confirm_meeting_slots # Bot confirms details
  - intent: affirm
  - action: action_schedule_meeting # Custom action to schedule
  - action: utter_goodbye

- story: Meeting scheduling - user provides all info upfront
  steps:
  - intent: schedule_meeting
    entities:
    - date: "next Monday"
    - time: "10 AM"
    - attendees: "Alice and Bob"
    - location: "Conference Room 1"
  - slot_was_set:
    - date: "next Monday"
  - slot_was_set:
    - time: "10 AM"
  - slot_was_set:
    - attendees: ["Alice", "Bob"]
  - slot_was_set:
    - location: "Conference Room 1"
  - action: schedule_meeting_form
  - active_loop: schedule_meeting_form
  - active_loop: null # All required slots were filled from intent
  - slot_was_set:
    - requested_slot: null
  - action: utter_confirm_meeting_slots
  - intent: affirm
  - action: action_schedule_meeting
  - action: utter_happy

- story: Meeting scheduling - user changes their mind about a slot
  steps:
  - intent: schedule_meeting
  - action: schedule_meeting_form
  - active_loop: schedule_meeting_form
  - slot_was_set:
    - requested_slot: date
  - intent: inform
    entities:
    - date: "today"
  - slot_was_set:
    - date: "today"
  - action: schedule_meeting_form
  - slot_was_set:
    - requested_slot: time
  - intent: inform
    entities:
    - time: "5pm"
  - slot_was_set:
    - time: "5pm"
  - action: schedule_meeting_form # Form asks for attendees
  - slot_was_set:
    - requested_slot: attendees
  - intent: inform
    entities:
    - attendees: "Just me"
  - slot_was_set:
    - attendees: ["Just me"]
  - action: schedule_meeting_form
  - active_loop: null
  - slot_was_set:
    - requested_slot: null
  - action: utter_confirm_meeting_slots
  - intent: deny # User wants to change something
  - action: utter_ask_what_to_change # (You'll need to define this response)
  - intent: inform # User specifies new date
    entities:
    - date: "tomorrow"
  - slot_was_set: # This will re-trigger the form or you might need a custom action to handle changes
    - date: "tomorrow"
  - action: schedule_meeting_form # Reactivate form to re-validate/re-ask if needed
  - active_loop: schedule_meeting_form
  # ... continue flow until confirmed

- story: Happy path for password reset
  steps:
  - intent: greet
  - action: utter_greet
  - intent: reset_password
  - action: utter_ask_employee_id
  - intent: inform
    entities:
    - employee_id: "E12345"
  - slot_was_set:
    - employee_id: "E12345"
  - action: action_reset_password
  - action: utter_goodbye

- story: Password reset - provides ID upfront
  steps:
  - intent: reset_password
    entities:
    - employee_id: "E9876"
  - slot_was_set:
    - employee_id: "E9876"
  - action: action_reset_password
  - action: utter_happy

- story: User says goodbye
  steps:
  - intent: goodbye
  - action: utter_goodbye

- story: Bot challenge
  steps:
  - intent: bot_challenge
  - action: utter_iamabot

- story: Out of scope query
  steps:
  - intent: out_of_scope
  - action: utter_out_of_scope