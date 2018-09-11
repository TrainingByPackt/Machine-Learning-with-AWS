SELECT tt.topic, 
	tt.term, 
	tt.weight, 
	dt.docname,
    dt.proportion
FROM linkedTopicDB2.tech_xplore_topic_terms AS tt, 
	linkedTopicDB2.tech_xplore_doc_topics AS dt
WHERE tt.topic = dt.topic
ORDER BY topic ASC;