dev:
	cd docker && docker-compose -p twds_2024_mentorship up -d

stop:
	cd docker && docker-compose -p twds_2024_mentorship down