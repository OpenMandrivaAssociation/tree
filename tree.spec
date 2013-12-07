Summary:	Utility which displays a tree view of directory contents
Name:		tree
Version:	1.6.0
Release:	5
Group:		File tools
License:	GPLv2+
URL:		http://mama.indstate.edu/users/ice/tree/
Source0:	ftp://mama.indstate.edu/linux/tree/%{name}-%{version}.tgz
Patch0:		tree-1.5.1.1-nostrip.diff
Patch1:         tree-1.5.2.2-link-flags.patch

%description
The tree utility recursively displays the contents of directories in a
tree-like format.  Tree is basically a UNIX port of the tree DOS
utility.

Install tree if you think it would be useful to view the contents of
specified directories in a tree-like format.

%prep

%setup -q
%patch0 -p0 -b .nostrip
# %patch1 -p1 -b .linkflags

%build
%global optflags %{optflags} -Os
%serverbuild_hardened
%make CFLAGS="%{optflags} -Wall -DLINUX -D_LARGEFILE64_SOURCE -D_FILE_OFFSET_BITS=64" LDFLAGS="%{ldflags}"

%install

mkdir -p %{buildroot}/{%{_bindir},%{_sbindir},%{_mandir}/man1}

%makeinstall_std \
	BINDIR=%{buildroot}%{_bindir} \
	MANDIR=%{buildroot}%{_mandir}/man1

%files
%doc README LICENSE CHANGES
%{_bindir}/%{name}
%{_mandir}/man1/%{name}*


%changelog
* Sun Apr 22 2012 Oden Eriksson <oeriksson@mandriva.com> 1.6.0-1
+ Revision: 792658
- 1.6.0
- various fixes

* Fri May 06 2011 Oden Eriksson <oeriksson@mandriva.com> 1.5.3-3
+ Revision: 670729
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 1.5.3-2mdv2011.0
+ Revision: 608042
- rebuild

  + Sandro Cazzaniga <kharec@mandriva.org>
    - fix warning
    - fix licence

* Tue Dec 15 2009 Frederik Himpe <fhimpe@mandriva.org> 1.5.3-1mdv2010.1
+ Revision: 479102
- update to new version 1.5.3

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.5.2.2-2mdv2010.0
+ Revision: 427433
- rebuild

  + Guillaume Rousse <guillomovitch@mandriva.org>
    - new version

* Tue Dec 23 2008 Oden Eriksson <oeriksson@mandriva.com> 1.5.1.1-3mdv2009.1
+ Revision: 317902
- use %%optflags and %%ldflags
- don't strip

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 1.5.1.1-2mdv2009.0
+ Revision: 225872
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Sat Nov 10 2007 David Walluck <walluck@mandriva.org> 1.5.1.1-1mdv2008.1
+ Revision: 107372
- 1.5.1.1
- rename typo patch
- fix spelling in typo patch
- call %%{make}

* Wed Aug 29 2007 Oden Eriksson <oeriksson@mandriva.com> 1.5.1-1mdv2008.0
+ Revision: 73448
- rebuild


* Fri Feb 02 2007 Lenny Cartier <lenny@mandriva.com> 1.5.1-1mdv2007.0
+ Revision: 115912
- Update to 1.5.1 and regenerate patch
- Import tree

* Wed Dec 07 2005 Lenny Cartier <lenny@mandriva.com> 1.5.0-2mdk
- rebuild

* Thu Nov 18 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.5.0-1mdk
- 1.5.0
- drop P1 (fixed upstream)

* Tue Jun 08 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.4b3-3mdk
- fix gcc-3.4 build (P1)

* Tue Apr 20 2004 Michael Scherer <misc@mandrake.org> 1.4b3-2mdk 
- Birthday rebuild

