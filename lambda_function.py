### Required Libraries ###
import json
from datetime import datetime
from dateutil.relativedelta import relativedelta
from botocore.vendored import requests


### Functionality Helper Functions ###
def get_portfolio(intent_request):
    """
    Assess results to identify clients ideal investment portfolio.
    """
    liquidityRisk = get_slots(intent_request)["liquidityRisk"]
    experience = get_slots(intent_request)["experience"]
    returnImportance = get_slots(intent_request)["returnImportance"]
    riskTolerance = get_slots(intent_request)["riskTolerance"]
    fearIndex = get_slots(intent_request)["fearIndex"]
    portfolio = []
    education = []
    liquidityRisk=parse_int(liquidityRisk)
    experience=parse_int(experience)
    returnImportance=parse_int(returnImportance)
    riskTolerance=parse_int(riskTolerance)
    fearIndex=parse_int(fearIndex)
    tally = experience + returnImportance + riskTolerance + fearIndex
    # print(tally)
    # print(experience)
    # print(returnImportance)
    # print(riskTolerance)
    # print(fearIndex)
    if liquidityRisk > 2:
        liquidityRisk = 1
    else:
        liquidityRisk = 0
    if experience > 2:
        education = 1
    else:
        education = 0
    if liquidityRisk == 1 and education == 1:
        if tally <= 7:
            portfolio = "Conservative"
        elif tally > 7 and tally <= 11:
            portfolio = "Moderately Conservative"
        elif tally > 11 and tally <= 14:
            portfolio = "Moderately Aggressive"
        elif tally > 14 and tally <= 17:
            portfolio = "Aggressive"
        else:
            portfolio = "Extremely Aggressive"
    elif liquidityRisk == 1 and education == 0:
        if tally <= 8:
            portfolio = "Conservative"
        elif tally > 8 and tally <= 12:
            portfolio = "Moderately Conservative"
        elif tally > 12 and tally <= 16:
            portfolio = "Moderately Aggressive"
        else:
            portfolio = "Aggressive"
    elif liquidityRisk == 0 and education == 1:
        if tally <= 8:
            portfolio = "Moderately Conservative"
        elif tally > 8 and tally <= 12:
            portfolio = "Moderately Aggressive"
        elif tally > 12 and tally <= 16:
            portfolio = "Aggressive"
        else:
            portfolio = "Extremely Aggressive"
    elif liquidityRisk == 0 and education == 0:
        if tally <= 9:
            portfolio = "Moderately Conservative"
        elif tally > 9 and tally <= 15:
            portfolio = "Moderately Aggressive"
        else:
            portfolio = "Aggressive"
    return portfolio
    
def get_portfolio_returns(intent_request):
    """
    Source portfolio performance results multiplier
    """
    portfolio = get_portfolio(intent_request)
    returns = 0
    if portfolio == "Conservative":
        returns = 0.01
    elif portfolio == "Moderately Conservative":
        returns = 0.05
    elif portfolio == "Moderately Aggressive":
        returns = 0.1
    elif portfolio == "Aggressive":
        returns = 0.15
    else:
        returns = 0.2
    return returns

def parse_int(n):
    """
    Securely converts a non-integer value to integer.
    """
    try:
        return int(n)
    except:
        return float("nan")

def parse_float(n):
    """
    Securely converts a non-numeric value to float.
    """
    try:
        return float(n)
    except:
        return float("nan")

def build_validation_result(is_valid, violated_slot, message_content):
    """
    Defines an internal validation message structured as a python dictionary.
    """
    if message_content is None:
        return {"isValid": is_valid, "violatedSlot": violated_slot}

    return {
        "isValid": is_valid,
        "violatedSlot": violated_slot,
        "message": {"contentType": "PlainText", "content": message_content},
    }
    
def validate_data(whatDOB, amount, intent_request):
    """
    Validates the data provided by the user.
    """
    whatDOB = get_slots(intent_request)["whatDOB"]
    amount = get_slots(intent_request)["amount"]
    # Validate that the user is over 18 years old
    if whatDOB is not None:
        birth_date = datetime.strptime(whatDOB, "%Y-%m-%d")
        age = relativedelta(datetime.now(), birth_date).years
        if age < 18:
            return build_validation_result(
                False,
                "whatDOB",
                "You should be at least 18 years old to use this service, "
                "Unfortunately we cannot help you at this time.",
            )
    # Validate the investment amount, it should be > 0 and < netWorth
    if amount is not None:
        amount = parse_float(amount)
        # Since parameters are strings it's important to cast values
        netWorth = get_slots(intent_request)["netWorth"]
        netWorth = parse_float(netWorth)
        if amount <= 0:
            return build_validation_result(
                False,
                "amount",
                "The amount to invest should be greater than zero, "
                "please provide a greater amount in dollars to invest.",
            )
        elif amount > netWorth:
            return build_validation_result(
                False,
                "amount",
                "The amount to invest should be less than your total net worth, "
                "please provide a lower amount in dollars to invest.",
            )

    # A True results is returned if age or amount are valid
    return build_validation_result(True, None, None)


### Dialog Actions Helper Functions ###
def get_slots(intent_request):
    """
    Fetch all the slots and their values from the current intent.
    """
    return intent_request['currentIntent']['slots']

def elicit_slot(session_attributes, intent_name, slots, slot_to_elicit, message):
    """
    Defines an elicit slot type response.
    """

    return {
        "sessionAttributes": session_attributes,
        "dialogAction": {
            "type": "ElicitSlot",
            "intentName": intent_name,
            "slots": slots,
            "slotToElicit": slot_to_elicit,
            "message": message,
        },
    }

def delegate(session_attributes, slots):
    """
    Defines a delegate slot type response.
    """

    return {
        "sessionAttributes": session_attributes,
        "dialogAction": {"type": "Delegate", "slots": slots},
    }

def close(session_attributes, fulfillment_state, message):
    """
    Defines a close slot type response.
    """

    response = {
        "sessionAttributes": session_attributes,
        "dialogAction": {
            "type": "Close",
            "fulfillmentState": fulfillment_state,
            "message": message,
        },
    }

    return response


### Intents Handlers ###
def simulate_performance(intent_request):
    """
    Performs hypothetical simulation of funds performance over a predetermined timeframe
    """

    # Gets slots' values
    amount = get_slots(intent_request)["amount"]
    whatDOB = get_slots(intent_request)["whatDOB"]
    portfolio_returns = get_portfolio_returns(intent_request)

    # Gets the invocation source, for Lex dialogs "DialogCodeHook" is expected.
    source = intent_request["invocationSource"]

    if source == "DialogCodeHook":
        # This code performs basic validation on the supplied input slots.

        # Gets all the slots
        slots = get_slots(intent_request)

        # Validates user's input using the validate_data function
        validation_result = validate_data(whatDOB, amount, intent_request)

        # If the data provided by the user is not valid,
        # the elicitSlot dialog action is used to re-prompt for the first violation detected.
        if not validation_result["isValid"]:
            slots[validation_result["violatedSlot"]] = None  # Cleans invalid slot

            # Returns an elicitSlot dialog to request new data for the invalid slot
            return elicit_slot(
                intent_request["sessionAttributes"],
                intent_request['currentIntent']['name'],
                slots,
                validation_result["violatedSlot"],
                validation_result["message"],
            )

        # Fetch current session attributes
        output_session_attributes = intent_request["sessionAttributes"]

        # Once all slots are valid, a delegate dialog is returned to Lex to choose the next course of action.
        return delegate(output_session_attributes, get_slots(intent_request))

    # Get the performance results
    returns = get_portfolio_returns(intent_request)
    percent_returns = returns * 100
    investment_value = parse_float(amount) * (1+returns)
    investment_value = round(investment_value, 2)

    # Return a message with investment results.
    return close(
        intent_request["sessionAttributes"],
        "Fulfilled",
        {
            "contentType": "PlainText",
            "content": """Thank you for your information;
            your simulated portfolio is at ${} for your ${} in initial investment. You realized
            {}% return on your investment.
            """.format(
                investment_value, amount, percent_returns
            ),
        },
    )

### Intents Dispatcher ###
def dispatch(intent_request):
    """
    Called when the user specifies an intent for this bot.
    """
    print(intent_request)
    # Get the name of the current intent
    intent_name = intent_request['currentIntent']['name']

    # Dispatch to bot's intent handlers
    if intent_name == "openAccount":
        return simulate_performance(intent_request)

    raise Exception("Intent with name " + intent_name + " not supported")
    

### Main Handler ###
def lambda_handler(event, context):
    """
    Route the incoming request based on intent.
    The JSON body of the request is provided in the event slot.
    """

    return dispatch(event)