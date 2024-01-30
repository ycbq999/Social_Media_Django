install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt


# install_node:
# 	curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.38.0/install.sh | bash
# 	export NVM_DIR="$HOME/.nvm"
# 	[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
# 	nvm install node

# install npm:
# 	sudo apt install npm

# install_tailwind:
# 	cd socialproject && npm init -y
# 	cd socialproject && npm install tailwindcss@2.2.16
# 	cd socialproject && npx tailwindcss init




# test:
# 	python -m pytest -vv test_*.py

format:
	black *.py

lint:
	pylint --disable=R,C project_content/app/*.py

all: install lint #test