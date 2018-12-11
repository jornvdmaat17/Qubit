# MultiQubit simulator

This repo can be used to simulate a MultiQubit system with a JSON file. 
The are a few different ways you can use this MultiQubit simulation, which are explained below.

## Generate your JSON
Firstly, if JSON is still a bit difficult for you to understand, you can use the makeMulti.html file to generate your own JSON.
You will be able to copy this JSON file to the multi.json file and run the multiJSONParser.py file. The pyton file will automaticly run the generated JSON file and print its outcome to screen.

## Make your own JSON
Secondly, you could also make your own JSON file, which will be faster to correct or add small things. After this the process of generating your output will be exectly the same as the first explained method. After you put your JSON in the multi.json file, just run multiJSONParser.py and your output will be displayed.


## JSON file explanation
Below follows an explanation of all the different parameters in the JSON file. The standard format of the JSON looks like this:

```JSON
{
	"multi": [
		{
			"qubits" : [],
			"paulix" : [],
			"pauliy" : [],
			"pauliz" : [],
			"hadamard" : [],
			"sqrnot" : [],
			"rphi" : {
				"index" : [],
				"phi" : 1
			},
			"print" : "false"
		}
	]
}
```

All the different paramaters can be erased except for "qubits" because otherwise you won't even have Qubits in your MultiQubit system.
Below I will go along every paramater and explain how to input values in there for your MultiQubit system.

# qubits

In here 

