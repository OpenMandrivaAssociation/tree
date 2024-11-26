Summary:	Utility which displays a tree view of directory contents

Name:		tree
Version:	2.2.1
Release:	1
Group:		File tools
License:	GPLv2+
URL:		https://oldmanprogrammer.net/source.php?dir=projects/tree
Source0:	https://oldmanprogrammer.net/tar/tree/tree-%{version}.tgz
Patch1:         tree-1.5.2.2-link-flags.patch

%description
The tree utility recursively displays the contents of directories in a
tree-like format.  Tree is basically a UNIX port of the tree DOS
utility.

Install tree if you think it would be useful to view the contents of
specified directories in a tree-like format.

%prep

%setup -q

%build
%make_build CFLAGS="%{optflags} -Wall -DLINUX -D_LARGEFILE64_SOURCE -D_FILE_OFFSET_BITS=64" LDFLAGS="%{ldflags}"

%install
mkdir -p %{buildroot}/{%{_bindir},%{_sbindir},%{_mandir}/man1}

%make_install \
	DESTDIR=%{buildroot}%{_bindir} \
	MANDIR=%{buildroot}%{_mandir}

%files
%doc README LICENSE CHANGES
%{_bindir}/%{name}
%{_mandir}/man1/%{name}*
