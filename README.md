## Dependencies

- All project dependencies can be installed by running the following command from within the `src` directory
  - `pip install -r requirements.txt`
- A list of non-native dependencies:
  - `json_stream`

## Execution Instructions

- To run the code run the following command from within the `src` directory
  - `python3 main.py`
- To execute the tests run the following command from within the `src` directory
  - `python3 run_tests.py`

## Design Decisions

- As a general design principle, I adhered to core OOP and SOLID principles to the best of my abilities
- I added a DEBUG environment variable
  - This both makes debugging easier if turned on and reduces costly logging if turned off
- I used the cached_property decorator
  - This allows for basic caching of property functions--AKA memoization--therefore significantly reducing the number of times each associated function is called
- I used dataclasses to hold string constants, making them much easier to change in the future if need be
- I used the `json_stream` package over the native `json` package
  - The benefit here is `json_stream.load()` loads in json data one line at a time, whereas `json.load()` loads the entire JSON document into memory at once
  - This allows the code to ingest much larger JSON files without concern for memory usage
- I chose to instantiate parent classes when initializing child classes instead of using inheritence
  - In python the super() method can lead to ambiguity and often tight coupling when multiple classes are inherited
  - Therefore in Python specifically it is my belief that it is best to avoid its use
- On line 57 of `urls.py` I redefined a function
  - In the initial function there is validation that has to be run only on the initial execution of the loop
  - Redefining the function allows us to avoid the overhead of subsequent if statements for the rest of the loop executions

## Future Additions

- I did not want to over-architect the solution simply for the sake of doing so, but here are a list of additions which could be made:
  - A parameter parser
  - A selection of sorting, filtering, and paging options for the data
  - The ability to handle file types other than csv and json for the encodes and decodes files
  - The ability to ingest the click and link data from sources other than files
  - An API framework built around the functionality
  - A Dockerfile to build an image of the code
  - A CI/CD pipeline which runs all tests, and if they pass builds the image using the Dockerfile and pushes it to a remote repository
