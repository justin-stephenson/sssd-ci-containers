Name:           ci-sssd
Version:        1
Release:        %autorelease
Summary:        SSSD CI Packages
URL:            https://github.com/SSSD/sssd-ci-containers

License:        GPLv3+
Source0:        random.c
Source1:        sss_pac_responder_client.c

BuildRequires: gcc
BuildRequires: openssl-devel

%description
SSSD CI Packages. For testing purpose only.

%prep

%build
gcc -fPIC -shared -o random.so %{SOURCE0} -lcrypto
gcc -o sss_pac_responder_client %{SOURCE1} -ldl -lpthread

%install
mkdir -p %{buildroot}/opt
cp random.so  %{buildroot}/opt/random.so
cp sss_pac_responder_client  %{buildroot}/opt/sss_pac_responder_client

%package test-deps
Summary: random.so for passkey testing and sss_pac_responder_client.

%description test-deps
random.so for passkey testing and sss_pac_responder_client.

%files test-deps
/opt/random.so
/opt/sss_pac_responder_client

%changelog
%autochangelog
