
NAME=qconf-agent
VERSION=1.0.0
PHPEXT_NAME=php-qconf-agent
FILES=agent base CMakeLists.txt  doc LICENSE README.md AUTHORS deps driver README_ZH.md  test
pkg:
	rm -rf ${NAME}-${VERSION}
	mkdir ${NAME}-${VERSION}
	cp -r ${FILES} ${NAME}-${VERSION}/
	tar -czf ${HOME}/rpmbuild/SOURCES/${NAME}-${VERSION}.tgz ${NAME}-${VERSION}
	rpmbuild -bb ${NAME}.spec
	rm -rf ${NAME}-${VERSION}


php:
	rm -rf ${PHPEXT_NAME}-${VERSION}
	mkdir ${PHPEXT_NAME}-${VERSION}
	cp -r driver/php/* ${PHPEXT_NAME}-${VERSION}
	tar -czf ${HOME}/rpmbuild/SOURCES/${PHPEXT_NAME}-${VERSION}.tgz ${PHPEXT_NAME}-${VERSION}
	rpmbuild -bb ${PHPEXT_NAME}.spec
	rm -rf ${PHPEXT_NAME}-${VERSION}
