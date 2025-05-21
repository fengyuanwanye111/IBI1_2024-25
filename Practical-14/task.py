import xml.dom.minidom  # Import DOM parser from standard library
import xml.sax  # Import SAX parser from standard library
from datetime import datetime  # Import datetime for time measurement
import os

os.chdir("Practical-14")

# DOM Implementation
print("Starting DOM parsing...")  # Indicate the start of DOM processing
start_time = datetime.now()  # Record the start time for performance measurement
dom_tree = xml.dom.minidom.parse("go_obo.xml")  # Parse the XML file into a DOM tree
collection = dom_tree.documentElement  # Get the root element of the DOM tree (e.g., <obo>)
terms = collection.getElementsByTagName("term")  # Get all <term> elements as a list

# Initialize a dictionary to store the term with maximum depth for each namespace
max_depth_terms = {
    "molecular_function": {"term": "", "count": 0},  # Store term name and count for molecular_function
    "biological_process": {"term": "", "count": 0},  # Store term name and count for biological_process
    "cellular_component": {"term": "", "count": 0}   # Store term name and count for cellular_component
}

# Iterate over each term to find the maximum depth
for term in terms:
    namespace = term.getElementsByTagName("namespace")[0].firstChild.nodeValue  # Get the namespace text
    if namespace not in max_depth_terms:  # Skip if namespace is not one of the target ontologies
        continue
    is_a_elements = term.getElementsByTagName("is_a")  # Get all <is_a> elements for this term
    is_a_count = len(is_a_elements)  # Count the number of <is_a> elements (depth)
    if is_a_count > max_depth_terms[namespace]["count"]:  # Update if current count is higher
        max_depth_terms[namespace]["term"] = term.getElementsByTagName("name")[0].firstChild.nodeValue  # Update term name
        max_depth_terms[namespace]["count"] = is_a_count  # Update maximum count

# Print results for each namespace
for namespace, data in max_depth_terms.items():
    print(f"{namespace.replace('_', ' ').capitalize()} - Term: {data['term']}, Max Depth: {data['count']}")

end_time = datetime.now()  # Record the end time
dom_time = (end_time - start_time).total_seconds()  # Calculate execution time in seconds
print(f"DOM execution time: {dom_time} seconds")  # Output the DOM execution time

# SAX Implementation
print("\nStarting SAX parsing...")  # Indicate the start of SAX processing
start_time = datetime.now()  # Record the start time for SAX performance measurement

# Define a custom handler for SAX parsing
class GOTermHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.current_tag = ""  # Track the current XML tag being processed
        self.current_name = ""  # Accumulate text content for name or namespace
        self.is_a_count = 0  # Count the number of <is_a> elements
        self.namespace = ""  # Store the current namespace
        self.max_depth_terms = {
            "molecular_function": {"term": "", "count": 0},  # Store max depth term for molecular_function
            "biological_process": {"term": "", "count": 0},  # Store max depth term for biological_process
            "cellular_component": {"term": "", "count": 0}   # Store max depth term for cellular_component
        }

    def startElement(self, tag, attributes):
        self.current_tag = tag  # Set the current tag
        if tag == "term":  # Reset counters and name when a new term starts
            self.is_a_count = 0
            self.current_name = ""

    def endElement(self, tag):
        if tag == "namespace":  # Store the namespace when the tag ends
            self.namespace = self.current_name.strip()  # Remove leading/trailing whitespace
        elif tag == "name":  # Store the term name
            self.current_name = self.current_name.strip()
        elif tag == "is_a":  # Increment the is_a count
            self.is_a_count += 1
        elif tag == "term" and self.namespace in self.max_depth_terms:  # Update max depth at term end
            if self.is_a_count > self.max_depth_terms[self.namespace]["count"]:
                self.max_depth_terms[self.namespace]["term"] = self.current_name  # Update term name
                self.max_depth_terms[self.namespace]["count"] = self.is_a_count  # Update max count
        self.current_tag = ""  # Reset current tag

    def characters(self, content):
        if self.current_tag in ["name", "namespace"]:  # Accumulate text for name or namespace
            self.current_name += content  # Append content (handles multi-line text)

# Set up and run the SAX parser
parser = xml.sax.make_parser()  # Create a SAX parser instance
parser.setFeature(xml.sax.handler.feature_namespaces, 0)  # Disable namespace processing for simplicity
handler = GOTermHandler()  # Instantiate the custom handler
parser.setContentHandler(handler)  # Set the handler for the parser
parser.parse("go_obo.xml")  # Parse the XML file, triggering events

# Print results for each namespace from SAX
for namespace, data in handler.max_depth_terms.items():
    print(f"{namespace.replace('_', ' ').capitalize()} - Term: {data['term']}, Max Depth: {data['count']}")

end_time = datetime.now()  # Record the end time for SAX
sax_time = (end_time - start_time).total_seconds()  # Calculate SAX execution time
print(f"SAX execution time: {sax_time} seconds")  # Output the SAX execution time

# Compare execution times and comment on which was faster
if dom_time < sax_time:
    print("# DOM ran faster")  # Comment indicating DOM was faster
else:
    print("# SAX ran faster")  # Comment indicating SAX was faster