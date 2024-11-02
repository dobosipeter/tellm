# TELLM  
  
TeLLM is a Python based terminal application used to communicate with remotely hosted LLMs through an inference API.  
_Using the OpenAI Python package and [Hyperbolic](https://hyperbolic.xyz/) Inference provider._  
  
## Usage  

Set the HYPERBOLIC_API_KEY environment variable.  
Install the dependencies  
Execute assistant.py  

## Feature Ideas  
  
* Manage conversations/sessions
    * Export, import? change between them
* Markdown print/display in terminal
* Tool use support for the models
    * Remember information about the user
    * Image input output
* Some kind of TUI?
    * Easily modify settings (inference provider, system prompt, etc.)
    * Better input text formatting
* Proper Python Package structure
    * Better terminal support
        * Execute using Python by default
        * Pass command line arguments
* Progress/waiting indicator while waiting for the model's response
    * If supported by the inference provider, enable streaming
* Support for multiple models, and switching between them easily.
