GIT_VERSION = $(shell git describe 2>/dev/null | sed 's/-/_/g')

ifneq ($(GIT_VERSION),)
GIT_CHECKOUT := true
endif

prep:
	dnf install -y git
	mkdir -p $(PWD)/rpmbuild/BUILD
	mkdir -p $(PWD)/rpmbuild/RPMS
	mkdir -p $(PWD)/rpmbuild/SOURCES
	mkdir -p $(PWD)/rpmbuild/SPECS
	mkdir -p $(PWD)/rpmbuild/SRPMS
	cp random.c $(PWD)/rpmbuild/SOURCES
	cp sss_pac_responder_client.c $(PWD)/rpmbuild/SOURCES
	cp ci-sssd.spec $(PWD)/rpmbuild/SPECS

srpm: prep
ifdef GIT_CHECKOUT
	sed -i "s/^Release:.*/Release: $(GIT_VERSION)/" ci-sssd.spec
endif
	rpmbuild --define "_topdir $(PWD)/rpmbuild" -bs ci-sssd.spec

rpms: prep
ifdef GIT_CHECKOUT
	sed -i "s/^Release:.*/Release: $(GIT_VERSION)/" ci-sssd.spec
endif
	rpmbuild --define "_topdir $(PWD)/rpmbuild" -ba ci-sssd.spec

clean:
	rm -fr $(PWD)/rpmbuild
