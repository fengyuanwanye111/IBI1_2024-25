# Pseudocode:
# BEGIN
#   ... (Import statements and directory setup as before) ...
#
#   3. DOM Implementation:
#      ...
#      f. Initialize a dictionary `dom_max_depth_terms` to store:
#         For each of "molecular_function", "biological_process", "cellular_component":
#           - "ids": A LIST of IDs of GO terms with the max <is_a> count.
#           - "term_names": A LIST of names of GO terms (optional, if needed, or just print IDs).
#           - "is_a_count": the maximum number of <is_a> tags.
#      g. Iterate through each "term" element:
#         ... (Extract id, name, namespace, is_a_count as before) ...
#         vii. If `is_a_count` is greater than the current maximum count for that namespace:
#              - Update "is_a_count" in `dom_max_depth_terms`.
#              - CLEAR the "ids" list for that namespace.
#              - ADD current_term_id to the "ids" list.
#              - (Optional: update "term_names" list similarly)
#         viii.ELSE IF `is_a_count` is EQUAL to the current maximum count for that namespace:
#              - ADD current_term_id to the "ids" list.
#              - (Optional: add current_term_name to "term_names" list)
#      h. Print the results (list of IDs and max is_a_count) for each namespace.
#      ...
#
#   4. SAX Implementation:
#      c. Define a SAX Content Handler class `GOTermHandler`:
#         i.   In `__init__`:
#              ...
#              - Initialize `sax_max_depth_terms` dictionary (similar to DOM, with "ids" as a list).
#         iv.  In `endElement(tag)`:
#              ...
#              - If `tag` is "term":
#                - If `current_term_namespace` is a target ontology:
#                  - If `is_a_count` > current max for `current_term_namespace`:
#                    - Update "is_a_count".
#                    - CLEAR "ids" list for `current_term_namespace`.
#                    - ADD `current_term_id` to "ids" list.
#                  - ELSE IF `is_a_count` == current max for `current_term_namespace`:
#                    - ADD `current_term_id` to "ids" list.
#      ...
#      e. Print results from `handler.sax_max_depth_terms` (showing list of IDs).
#   ...
# END

import xml.dom.minidom
import xml.sax
from datetime import datetime
import os

try:
    if "Practical-14" not in os.getcwd(): # Check if not already in the target directory
        os.chdir("Practical-14")
    print(f"Current working directory: {os.getcwd()}")
except FileNotFoundError:
    print("Error: Could not change directory to 'Practical-14'. Make sure the directory exists and the script is run from its parent directory.")
    exit()

xml_file = "go_obo.xml"

# --- DOM Implementation ---
print("\nStarting DOM parsing...")
start_time_dom = datetime.now()

dom_max_depth_terms = {
    "molecular_function": {"ids": [], "term_names": [], "is_a_count": 0}, # Store list of IDs and names
    "biological_process": {"ids": [], "term_names": [], "is_a_count": 0},
    "cellular_component": {"ids": [], "term_names": [], "is_a_count": 0}
}

try:
    dom_tree = xml.dom.minidom.parse(xml_file)
    collection = dom_tree.documentElement
    terms = collection.getElementsByTagName("term")

    for term_element in terms:
        try:
            namespace_nodes = term_element.getElementsByTagName("namespace")
            if not namespace_nodes or not namespace_nodes[0].firstChild:
                continue
            current_namespace = namespace_nodes[0].firstChild.nodeValue.strip()

            if current_namespace in dom_max_depth_terms:
                id_nodes = term_element.getElementsByTagName("id")
                name_nodes = term_element.getElementsByTagName("name")

                current_term_id = "Unknown ID"
                if id_nodes and id_nodes[0].firstChild:
                    current_term_id = id_nodes[0].firstChild.nodeValue.strip()

                current_term_name = "Unknown Term Name"
                if name_nodes and name_nodes[0].firstChild:
                    current_term_name = name_nodes[0].firstChild.nodeValue.strip()

                is_a_elements = term_element.getElementsByTagName("is_a")
                current_is_a_count = len(is_a_elements)

                if current_is_a_count > dom_max_depth_terms[current_namespace]["is_a_count"]:
                    dom_max_depth_terms[current_namespace]["is_a_count"] = current_is_a_count
                    dom_max_depth_terms[current_namespace]["ids"] = [current_term_id] # Reset list with new max
                    dom_max_depth_terms[current_namespace]["term_names"] = [current_term_name] # Reset list
                elif current_is_a_count == dom_max_depth_terms[current_namespace]["is_a_count"]:
                    if current_is_a_count > 0: # Only add if it's a valid count (not initial 0)
                        dom_max_depth_terms[current_namespace]["ids"].append(current_term_id) # Append to list for ties
                        dom_max_depth_terms[current_namespace]["term_names"].append(current_term_name)
        except Exception:
            continue

    print("\nDOM Parsing Results:")
    for namespace_key, data in dom_max_depth_terms.items():
        formatted_namespace = namespace_key.replace('_', ' ').capitalize()
        # Joining term names for display if you want, or just show IDs as per classmate's output
        # term_names_str = ", ".join(data['term_names'])
        print(f"{formatted_namespace}: IDs {data['ids']} with {data['is_a_count']} is_a elements")
        # If you want to include names:
        # print(f"{formatted_namespace} - IDs: {data['ids']}, Names: [{term_names_str}], Max <is_a> count: {data['is_a_count']}")


except FileNotFoundError:
    print(f"Error: XML file '{xml_file}' not found for DOM parsing.")
except Exception as e:
    print(f"An error occurred during DOM parsing: {e}")

end_time_dom = datetime.now()
dom_time_taken = (end_time_dom - start_time_dom).total_seconds()
print(f"DOM execution time: {dom_time_taken:.4f} seconds")


# --- SAX Implementation ---
print("\nStarting SAX parsing...")
start_time_sax = datetime.now()

class GOTermHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.current_tag = ""
        self.accumulated_id_content = ""
        self.accumulated_term_name_content = ""
        self.accumulated_namespace_content = ""

        self.current_term_is_a_count = 0
        self.current_term_actual_id = ""
        self.current_term_actual_namespace = ""
        self.current_term_actual_name = ""

        self.sax_max_depth_terms = {
            "molecular_function": {"ids": [], "term_names": [], "is_a_count": 0},
            "biological_process": {"ids": [], "term_names": [], "is_a_count": 0},
            "cellular_component": {"ids": [], "term_names": [], "is_a_count": 0}
        }

    def startElement(self, tag, attributes):
        self.current_tag = tag
        if tag == "term":
            self.current_term_is_a_count = 0
            self.accumulated_id_content = ""
            self.accumulated_term_name_content = ""
            self.accumulated_namespace_content = ""
            self.current_term_actual_id = ""
            self.current_term_actual_name = ""
            self.current_term_actual_namespace = ""

    def characters(self, content):
        if self.current_tag == "id":
            self.accumulated_id_content += content
        elif self.current_tag == "name":
            self.accumulated_term_name_content += content
        elif self.current_tag == "namespace":
            self.accumulated_namespace_content += content

    def endElement(self, tag):
        if tag == "id":
            self.current_term_actual_id = self.accumulated_id_content.strip()
            self.accumulated_id_content = ""
        elif tag == "name":
            self.current_term_actual_name = self.accumulated_term_name_content.strip()
            self.accumulated_term_name_content = ""
        elif tag == "namespace":
            self.current_term_actual_namespace = self.accumulated_namespace_content.strip()
            self.accumulated_namespace_content = ""
        elif tag == "is_a":
            self.current_term_is_a_count += 1
        elif tag == "term":
            if self.current_term_actual_namespace in self.sax_max_depth_terms:
                target_ns_data = self.sax_max_depth_terms[self.current_term_actual_namespace]
                if self.current_term_is_a_count > target_ns_data["is_a_count"]:
                    target_ns_data["is_a_count"] = self.current_term_is_a_count
                    target_ns_data["ids"] = [self.current_term_actual_id] # Reset list
                    target_ns_data["term_names"] = [self.current_term_actual_name] # Reset list
                elif self.current_term_is_a_count == target_ns_data["is_a_count"]:
                    if self.current_term_is_a_count > 0: # Only add if it's a valid count
                        target_ns_data["ids"].append(self.current_term_actual_id) # Append for ties
                        target_ns_data["term_names"].append(self.current_term_actual_name)
        
        self.current_tag = ""

try:
    parser = xml.sax.make_parser()
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)
    Handler = GOTermHandler()
    parser.setContentHandler(Handler)
    parser.parse(xml_file)

    print("\nSAX Parsing Results:")
    for namespace_key, data in Handler.sax_max_depth_terms.items():
        formatted_namespace = namespace_key.replace('_', ' ').capitalize()
        # term_names_str = ", ".join(data['term_names'])
        print(f"{formatted_namespace}: IDs {data['ids']} with {data['is_a_count']} is_a elements")
        # If you want to include names:
        # print(f"{formatted_namespace} - IDs: {data['ids']}, Names: [{term_names_str}], Max <is_a> count: {data['is_a_count']}")

except FileNotFoundError:
    print(f"Error: XML file '{xml_file}' not found for SAX parsing.")
except xml.sax.SAXParseException as e:
    print(f"Error parsing XML with SAX: {e}")
except Exception as e:
    print(f"An error occurred during SAX parsing: {e}")

end_time_sax = datetime.now()
sax_time_taken = (end_time_sax - start_time_sax).total_seconds()
print(f"SAX execution time: {sax_time_taken:.4f} seconds")

# --- Compare execution times ---
print("\n--- Performance Comparison ---")
if dom_time_taken < sax_time_taken:
    print(f"# DOM ran faster ({dom_time_taken:.4f}s vs {sax_time_taken:.4f}s for SAX)")
elif sax_time_taken < dom_time_taken:
    print(f"# SAX ran faster ({sax_time_taken:.4f}s vs {dom_time_taken:.4f}s for DOM)")
else:
    print(f"# DOM and SAX had similar execution times (DOM: {dom_time_taken:.4f}s, SAX: {sax_time_taken:.4f}s)")