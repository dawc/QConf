
NAME=qconf-agent
VERSION=1.0.0
FILES=agent base CMakeLists.txt  doc LICENSE README.md AUTHORS deps driver README_ZH.md  test
pkg:
	rm -rf ${NAME}-${VERSION}
	mkdir ${NAME}-${VERSION}
	cp -r ${FILES} ${NAME}-${VERSION}/
	tar -czf ${HOME}/rpmbuild/SOURCES/${NAME}-${VERSION}.tgz ${NAME}-${VERSION}
	rpmbuild -bb ${NAME}.spec
	rm -rf ${NAME}-${VERSION}
