SELECT dt.docname, 
	tt.topic,
    dt.proportion,
	tt.term, 
	tt.weight
FROM linkedTopicDB2.known_structure__topic_terms tt, linkedTopicDB2.known_structure__doc_topics dt
WHERE tt.topic = dt.topic
ORDER BY docname ASC;
 