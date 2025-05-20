from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, ActiveLoop
from rasa_sdk.types import DomainDict

class ActionScheduleMeeting(Action):
    def name(self) -> Text:
        return "action_schedule_meeting"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        date = tracker.get_slot('date')
        time = tracker.get_slot('time')
        location = tracker.get_slot('location')
        attendees = tracker.get_slot('attendees')

        attendees_text = ""
        if attendees:
            if isinstance(attendees, list):
                attendees_text = f" with {', '.join(attendees)}"
            else: # Should be a list from the slot type, but handle if string
                attendees_text = f" with {attendees}"
        else:
            attendees_text = " (no attendees specified)"


        location_text = f" in {location}" if location else " (no location specified)"
        date_text = date if date else "(no date specified)"
        time_text = time if time else "(no time specified)"

        # In a real scenario, you would integrate with a calendar API here.
        # For now, we'll just confirm and print to the action server console.
        confirmation_message = f"Okay, I've notionally scheduled the meeting for {date_text} at {time_text}{location_text}{attendees_text}."
        
        print(f"--- Meeting Scheduling Attempt ---")
        print(f"  Date: {date}")
        print(f"  Time: {time}")
        print(f"  Location: {location}")
        print(f"  Attendees: {attendees}")
        print(f"--- End Meeting Scheduling ---")

        dispatcher.utter_message(text=confirmation_message)

        # Clear slots after scheduling
        return [
            SlotSet("date", None),
            SlotSet("time", None),
            SlotSet("location", None),
            SlotSet("attendees", None),
            SlotSet("requested_slot", None) # Clear requested_slot from form
        ]

class ValidateScheduleMeetingForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_schedule_meeting_form"

    async def validate_date(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `date` value."""
        if not slot_value:
            dispatcher.utter_message(text="I need a date for the meeting.")
            return {"date": None}
        # Add more sophisticated date validation if needed (e.g., check format, ensure it's in the future)
        print(f"Validated date: {slot_value}")
        return {"date": slot_value}

    async def validate_time(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `time` value."""
        if not slot_value:
            dispatcher.utter_message(text="What time should the meeting be?")
            return {"time": None}
        # Add more sophisticated time validation if needed
        print(f"Validated time: {slot_value}")
        return {"time": slot_value}

    async def validate_attendees(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `attendees` value."""
        if not slot_value:
            dispatcher.utter_message(text="Who should attend the meeting?")
            return {"attendees": None}
        
        # Ensure attendees is a list
        if isinstance(slot_value, str):
            # A simple heuristic: if it contains "and" or ",", split it.
            # More robust parsing might be needed for complex inputs.
            if " and " in slot_value:
                validated_attendees = [a.strip() for a in slot_value.split(" and ")]
            elif "," in slot_value:
                validated_attendees = [a.strip() for a in slot_value.split(",")]
            else:
                validated_attendees = [slot_value.strip()]
        elif isinstance(slot_value, list):
            validated_attendees = slot_value
        else:
            dispatcher.utter_message(text="I couldn't understand the attendees list. Please list them separated by commas or 'and'.")
            return {"attendees": None}

        print(f"Validated attendees: {validated_attendees}")
        return {"attendees": validated_attendees}

    # Optional: Validate location if you make it a required slot
    # async def validate_location(
    #     self,
    #     slot_value: Any,
    #     dispatcher: CollectingDispatcher,
    #     tracker: Tracker,
    #     domain: DomainDict,
    # ) -> Dict[Text, Any]:
    #     """Validate `location` value."""
    #     if not slot_value:
    #         dispatcher.utter_message(text="Where will the meeting be held?")
    #         return {"location": None}
    #     print(f"Validated location: {slot_value}")
    #     return {"location": slot_value}


class ActionResetPassword(Action):
    def name(self) -> Text:
        return "action_reset_password"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        employee_id = tracker.get_slot('employee_id')

        if employee_id:
            # In a real application, you would integrate with an identity management system.
            message = f"A password reset link has been initiated for employee ID: {employee_id}. Please check your registered communication channels."
            print(f"--- Password Reset Attempt ---")
            print(f"  Employee ID: {employee_id}")
            print(f"--- End Password Reset ---")
        else:
            # This should ideally be caught by a form or a required slot question
            message = "I need your employee ID to reset your password. Could you please provide it?"
            dispatcher.utter_message(text=message)
            return [] # Don't clear employee_id slot if we're asking for it again

        dispatcher.utter_message(text=message)
        return [SlotSet("employee_id", None)]