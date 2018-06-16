all: gen create clean

clean:
	rm -f ./consumer_key ./consumer_secret ./access_token_key ./access_token_secret

create:
	kubectl create secret generic twitter-credentials --from-file=./consumer_key --from-file=./consumer_secret --from-file=./access_token_key --from-file=./access_token_secret

gen:
	python ./secret-gen.py .env

