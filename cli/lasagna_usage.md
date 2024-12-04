#### Click CLI

##### What is it?

##### Why are we using it?

##### Example

**Click Group** = `@click.group`
        
- In this example: `@chef_cmd`

**Click Command** = `@click.command`

- In this example:

    - `@chef_cmd("sous-chef")`

    - `@chef_cmd("head-chef")` 

    - `@chef_cmd("pastry-chef")`

**Click Option** = `@click.option`

- In this example: `@click.option("--name",default=" ", help=" ")`
    
- **(Name, Default, Help):**

    - *"--gordon-ramsay"*, Gordon Ramsay, Chef specializing in public image

    - *"--martha-stewart"*, Martha Stewart, Chef specializing in cross-cultural cuisine

    - *"--napoli-matfia"*, Napoli Matfia, Chef from Korea specializing in Italian 
        Cuisine

    - *"--ratatouille"*, Remy from Ratatoullie, Chef specializing in guidance and sense of smell

#### Syntax for click commands

- Use decorator `@click.command` to indicate you are creating a command.

- Click commands should include a description outlining their functionality

- Click uses decorators on top of typical python functions to extend functionality

- Decorators in Python can be created with wrapper functions that extend usage of functionality

**Example:** If you have a `@click.group` that you want to have specific options per command, but base level options that are present within every command, use decorators.

To create a decorator you want to have your regular function definition that has a wrapper function inside of it and for it to have a specified return type

**Note:** `(*args, **kwargs)` -> These are positional arguments (`*args`) and keyword arguments(`**kwargs`).

- This representation accounts for unknown numbers of accepted arguments but what is known is that there are several positional arguments and keyword arguments 

